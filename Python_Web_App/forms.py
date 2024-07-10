from django import forms
from Python_Web_App.models import *


class UserForm(forms.ModelForm):
    class Meta:
        model=User_Info
        fields='__all__'
