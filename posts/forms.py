from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML, ButtonHolder
from django import forms
from posts.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published', 'sponsored', 'image']
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
                    'image'
                ),
                ButtonHolder(
                    Submit('submit', 'Dodaj', css_class='btn btn-primary'),
                    css_class="d-flex justify-content-end"
                )
            )