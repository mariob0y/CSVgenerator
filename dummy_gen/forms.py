from django import forms
from django.db import models
from .models import Scheme


class SchemeForm(forms.ModelForm):
    class Meta:
        model = Scheme
        fields = ['name', 'author',
                  'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9',
                  'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 'n8', 'n9',
                  'o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8', 'o9',
                  'rows']
