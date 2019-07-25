from django import forms
from .models import Add

class AddForm(forms.ModelForm):
    class Meta:
        model = Add
        fields = '__all__'

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()