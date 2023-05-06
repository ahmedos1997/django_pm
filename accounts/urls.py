from django.urls import path, include
from django.contrib.auth.views import LoginView
from accounts.forms import userloginform
from accounts.views import registerview, editprofile

urlpatterns = [

    path('login/', LoginView.as_view(authentication_form=userloginform), name='login'),
    path('register/', registerview.as_view(), name='register'),
    path('profile/', editprofile, name='profile'),
    path('', include('django.contrib.auth.urls')),
]
