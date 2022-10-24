from dataclasses import fields
from distutils.filelist import FileList
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email' ]

class ProfileForm(forms.ModelForm):
    class Meta:
      model=Profile
      fields=['city','phone_number','image']
