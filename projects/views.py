from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class projectlistviews(LoginRequiredMixin,ListView):
    model = models.project
    template_name = 'project/list.html' # هذا اسم صفحة ال html
    paginate_by = 6
    def get_queryset(self):
        query_set = super().get_queryset()
        where = {'user_id': self.request.user} # عدم الظهور الى للمستخدم الحالي
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
    # سنستدعي بيانات المستخدم كجزء من بيانات الاستمارة مع وجود حقل مخصص لرقم المستخدم
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class projectupdateviews(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #ريجب مراعاة الترتيب
    model = models.project
    form_class = forms.projectupdateform
    template_name = 'project/update.html'
    success_url = reverse_lazy('project_list')

    # دالة للتاكد من بيانات المستخدم قبل عرض الصفحة
    def test_func(self):
        return self.get_object().user_id == self.request.user.id # هنا حددنا التاكد من رقم المستخدم في المشروع مع رقم المستخدم الموجود حاليا
    def get_success_url(self):               # تعيد صفحة معينة في حالة نجاح العملية
        return reverse ('project_update', args=[self.object.id])  # مررنا id  المشروع كمعامل للدالة حيث object يعبر عن المشروع project



class projectdeleteview(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = models.project
    template_name = 'project/delete.html'
    def test_func(self):
        return self.get_object().user_id == self.request.user.id
    success_url = reverse_lazy('project_list')





class taskcraeteview(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = models.task
    fields = ['project','description']
    http_method_names = ['post']  # حددنا له ان الصفحة موجودة ولكن لغرض ال post فقط

    def test_func(self):
        project_id = self.request.POST.get('project','')
        return models.project.objects.get(pk=project_id).user_id == self.request.user.id

    def get_success_url(self):
        return reverse ('project_update', args=[self.object.project.id])


class taskupdateview(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = models.task
    fields = ['is_completed']
    http_method_names = ['post']
    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id
    def get_success_url(self):
        return reverse ('project_update', args=[self.object.project.id])



class taskdeleteview(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = models.task
    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id
    def get_success_url(self):
        return reverse ('project_update', args=[self.object.project.id])




