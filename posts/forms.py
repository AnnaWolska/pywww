from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML, ButtonHolder
from django import forms
from dal import autocomplete
from posts.models import Post, Category
from tags.models import Tag
from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelectMultiple


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tags:tag-autocomplete'
        ))
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        # widget=AutocompleteSelectMultiple(Post._meta.get_field('categories'),admin.AdminSite())
        widget=autocomplete.ModelSelect2Multiple(url='posts:category-autocomplete'
        ))

    class Meta:
        model = Post
        fields = ['title', 'content', 'published', 'sponsored', 'image', 'tags', 'categories']
        labels = {
            "title": "Tytuł",
            "content": "Treść",
            "published": "Opublikowany",
            "sponsored": "Sponsorowany"
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.from_action = 'post:add'
            self.helper.layout = Layout(
                Fieldset(
                    'Dodaj post',
                    'title',
                    'content',
                    'published',
                    'sponsored',
                    'image',
                    'tags',
                    'categories',
                ),
                ButtonHolder(
                    Submit('submit', 'Dodaj', css_class='btn btn-primary'),
                    css_class="d-flex justify-content-end"
                )
            )