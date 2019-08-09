from django.forms import ModelForm
from .models import input
from django import forms

class inputForm(ModelForm):
    class Meta:
        model = input
        fields = '__all__'
        widgets = {
            'link': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : "Enter Amazon Link"
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Your Price"
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Enter Your Email"
                }
            ),
        }