from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class projectlistviews(LoginRequiredMixin,ListView):
    model = models.project
    template_name = 'project/list.html' # هذا اسم صفحة ال html
    paginate_by = 6
    def get_queryset(self):
        query_set = super().get_queryset()
        where = {}
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)



# Create your views here.

class projectcreateviews(LoginRequiredMixin,CreateView):
    model = models.project
    form_class = forms.projectcreateform
    template_name = 'project/create.html'
    success_url = reverse_lazy('project_list')


class projectupdateviews(LoginRequiredMixin,UpdateView):
    model = models.project
    form_class = forms.projectupdateform
    template_name = 'project/update.html'
    success_url = reverse_lazy('project_list')
    def get_success_url(self):               # تعيد صفحة معينة في حالة نجاح العملية
        return reverse ('project_update', args=[self.object.id])  # مررنا id  المشروع كمعامل للدالة حيث object يعبر عن المشروع project




class projectdeleteview(LoginRequiredMixin,DeleteView):
    model = models.project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('project_list')





class taskcraeteview(LoginRequiredMixin,CreateView):
    model = models.task
    fields = ['project','description']
    http_method_names = ['post']  # حددنا له ان الصفحة موجودة ولكن لغرض ال post فقط
    def get_success_url(self):
        return reverse ('project_update', args=[self.object.project.id])


class taskupdateview(LoginRequiredMixin,UpdateView):
    model = models.task
    fields = ['is_completed']
    http_method_names = ['post']
    def get_success_url(self):
        return reverse ('project_update', args=[self.object.project.id])



class taskdeleteview(LoginRequiredMixin,DeleteView):
    model = models.task
    def get_success_url(self):
        return reverse ('project_update', args=[self.object.project.id])




