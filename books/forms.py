from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML, ButtonHolder
from django import forms
from books.models import Books

class BookForm(forms.ModelForm):
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