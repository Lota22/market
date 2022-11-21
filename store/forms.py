from django import forms 
from django.forms import ModelForm
from . models import *

class CartForms(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']