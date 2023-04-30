from django import forms
from . import models

class projectcreateform(forms.ModelForm):
    class Meta:
        model = models.project
        fields = ['category', 'title', 'description']
        widgets = {
            'category': forms.Select(),
            'title': forms.TextInput(),
            'description': forms.Textarea()
        }

class projectupdateform(forms.ModelForm):
    class Meta:
        model = models.project
        fields = ['category', 'title', 'status']
        widgets = {
            'category': forms.Select(),
            'title': forms.TextInput(),
            'status': forms.Select()
        }
