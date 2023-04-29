from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.projectlistviews.as_view(), name='project_list'), # هذه الاسم سنستخدمه لاحقا
    path('project/create', views.projectcreateviews.as_view(), name='project_create')
]
