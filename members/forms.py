from django.shortcuts import render
from .forms import FormContactForm
from django import forms
from .models import form

class forms_(forms.ModelForm):
    class Meta:
        model=form
        fields="__all__"