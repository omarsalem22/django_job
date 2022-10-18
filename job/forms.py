from dataclasses import Field
from pyexpat import model
from django import forms
from .models import Apply

class Applyform(forms.ModelForm):
    class Meta:
        model=Apply
        fields=[ 'name', 'email','website','cv','cover_letter']