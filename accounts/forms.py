from django.contrib.auth.forms import AuthenticationForm
from django import forms

attrs = {'class': 'form-control'}


class userloginform(AuthenticationForm):
    def __int__(self, *args, **kwargs):        # حددنا الدالة البانية
        super(userloginform, self).__init__(*args, **kwargs)      # استدعينا الدالة البانية للصنف الاب

    username = forms.CharField(
        label= 'username',
        widget=forms.TextInput(attrs=attrs)
    )

    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs=attrs)
    )
