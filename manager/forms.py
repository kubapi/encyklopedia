from django import forms
from .models import Entry
from django.utils.text import slugify


class EntryCreateForm(forms.ModelForm):
    class Meta:
        model = Entry
        exclude = ('slug', 'search_count', 'status')
        widgets = {
                'word': forms.TextInput(attrs={'placeholder': 'Hasło'}),
                'definition': forms.Textarea(
                    attrs={'placeholder': 'Definicja'}),
            }
        labels = {
        "word": "Podaj hasło:",
        "definition": "Podaj definicje:"
        }