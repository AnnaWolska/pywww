from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML, ButtonHolder
from django import forms
from books.models import Books, Author
from dal import autocomplete
from tags.models import Tag
from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelectMultiple


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


AuthorFormSet = forms.modelformset_factory(Author, form=AuthorForm)


class BookForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tags:tag-autocomplete')
    )
    author = forms.ModelChoiceField(queryset=Author.objects.all(), required=False)

    class Meta:
        model = Books
        fields = ['title', 'decription', 'available', 'publication_year', 'author', 'tags', "image"]
        labels = {
            "title": "Tytuł",
            "decription": "opis",
            "available": "dostępność",
            "publication_year": "rok",
            "author" : "autor",
            "tags":"tagi",
            "image" : "obraz"
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.from_method = 'post'
            self.helper.from_method = 'books:add'
            # to jest dwa razy metod i działa, nie ma action, o co chodzi?
            self.helper.layout = Layout(
                Fieldset(
                    'Dodaj książkę',
                    'title',
                    'decription',
                    'available',
                    'publication_year',
                    'author',
                    'tags',
                    'image'
                ),
                ButtonHolder(
                    Submit('submit', 'Dodaj', css_class='btn btn-primary'),
                    css_class="d-flex justify-content-end"
                )
            )


class BookBorrowForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('borrow', 'Wypożycz'))




