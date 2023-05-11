from django.contrib import admin
from django.urls import path , include
from . import views



admin.site.site_header = ('Project Management')
admin.site.site_title = ('Project Management')



urlpatterns = [
    path('',views.projectlistviews.as_view(), name='project_list'), # هذه الاسم سنستخدمه لاحقا
    path('project/create', views.projectcreateviews.as_view(), name='project_create'),
    path('project/edite/<int:pk>', views.projectupdateviews.as_view(), name='project_update'),
    path('project/delete/<int:pk>', views.projectdeleteview.as_view(), name='project_delete'),
    path('task/create', views.taskcraeteview.as_view(), name='task_create'),
    path('task/edite/<int:pk>', views.taskupdateview.as_view(), name='task_update'),
    path('task/delete/<int:pk>', views.taskdeleteview.as_view(), name='task_delete'),

]
