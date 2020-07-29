from django.forms import ModelForm, Textarea

from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'class':'form-input'})
        }
    def __init__(self, *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        self.fields['text'].widget.attrs.update({'class':'form-input'})

    def save(self, commit=True, text=""):
        instance = super(CommentForm, self).save(commit=commit)
        instance.text = "NO podras modificarme"
        if commit:
            instance.save()

from django import forms
from django.core.validators import MinLengthValidator, EmailValidator
class ContactForm(forms.Form):
    name = forms.CharField(required=True, validators=[MinLengthValidator(2, message="'Muy corto! (minimo %(limit_value)d) actual:%(show_value)d")])
    email = forms.CharField(label='Correo', validators=[EmailValidator(message='Correo invalido', whitelist=['gmail'])])
    # max_length=10, min_length=3 validators=[MinLengthValidator(2)]
    # surname = forms.CharField(initial='Pepe', required=False, max_length=10, min_length=3)
    # phone = forms.RegexField(label='Telefono', required=True, regex='\(\w{3}\)\w{3}-\w{4}', max_length=13, min_length=13)
    # date_birth = forms.DateField(label='Fecha de Nacimiento')


