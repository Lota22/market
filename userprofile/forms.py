from random import choices
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

STATE = [
    ('Ondo','Ondo'),
    ('Ogun','Ogun'),
    ('Kwara','Kwara'),
    ('Anambra','Anambra'),
    ('Osun','Osun'),
    ('Oyo','Oyo'),
    ('Delta','Delta'),
]

GENDER =[
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
]

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name', 'email', 'phone', 'address', 'state', 'gender', 'nationality', 'pix']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Phone No.'}),
            'Address': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Address'}),
            'state': forms.Select(attrs={'class':'form-control'}, choices = STATE),
            'gender': forms.Select(attrs={'class':'form-control'}, choices = GENDER),
            'nationality': forms.Select(attrs={'class':'form-control', 'placeholder': 'Nationality'}),
            'pix': forms.FileInput(attrs={'class':'form-control'}),
        }        
        
