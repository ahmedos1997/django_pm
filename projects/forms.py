from django import forms
from . import models

attrs = {'class': 'form-control'}

class projectcreateform(forms.ModelForm):
    class Meta:
        model = models.project
        fields = ['category', 'title', 'description']
        widgets = {
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'description': forms.Textarea(attrs=attrs)
        }

class projectupdateform(forms.ModelForm):
    class Meta:
        model = models.project
        fields = ['category', 'title', 'status']
        widgets = {
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'status': forms.Select(attrs=attrs)
        }
