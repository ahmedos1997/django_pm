from django.shortcuts import render
from django.views.generic import ListView, CreateView
from . import models
from . import forms
from django.urls import reverse_lazy


class projectlistviews(ListView):
    model = models.project
    template_name = 'project/list.html' # هذا اسم صفحة ال html


# Create your views here.

class projectcreateviews(CreateView):
    model = models.project
    form_class = forms.projectcreateform
    template_name = 'project/create.html'
    success_url = reverse_lazy('project_list')
