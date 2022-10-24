from dataclasses import Field, field, fields
from pyexpat import model
from django import forms
from .models import *

class Applyform(forms.ModelForm):
    class Meta:
        model=Apply
        fields=[ 'name', 'email','website','cv','cover_letter']
class Job_form(forms.ModelForm):
    class Meta:
        model=Job
        fields='__all__' 
        exclude= ('slug','owner',)    