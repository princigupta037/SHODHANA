
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField()
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'mobile'
        ]
