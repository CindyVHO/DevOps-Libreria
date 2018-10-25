from django import forms
from .models import Libro
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('nombre', 'autor', 'isbn', 'urlImagen', 'editorial', 'anioPublicacion')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit', 'Guardar Libro'))