from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


attrs = {'class': 'form-control'}


class userloginform(AuthenticationForm):
    def __int__(self, *args, **kwargs):        # حددنا الدالة البانية
        super(userloginform, self).__init__(*args, **kwargs)      # استدعينا الدالة البانية للصنف الاب

    username = forms.CharField(
        label= _('username'),
        widget=forms.TextInput(attrs=attrs)
    )

    password = forms.CharField(
        label=_('password'),
        widget=forms.PasswordInput(attrs=attrs)
    )


class userregisterform(UserCreationForm):

    first_name = forms.CharField(
        label=_('First Name'),
        widget=forms.TextInput(attrs=attrs)
    )

    last_name = forms.CharField(
        label=_('Last Name'),
        widget=forms.TextInput(attrs=attrs)
    )
    username = forms.CharField(
        label=_('User Name'),
        widget=forms.TextInput(attrs=attrs)
    )

    email = forms.EmailField(
        label=_('Email'),
        widget=forms.TextInput(attrs=attrs)
    )

    password1 = forms.CharField(
        label=_('password'),
        strip=False,
        widget=forms.PasswordInput(attrs=attrs)
    )

    password2 = forms.CharField(
        label=_('password confirmation'),
        strip=False,
        widget=forms.PasswordInput(attrs=attrs)
    )

    class Meta(UserCreationForm.Meta):   # تعريف الحقول المطلوبة باستخدام meta
        fields = ('first_name', 'last_name', 'username', 'email')

class profileform(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name' : forms.TextInput(attrs=attrs),
            'last_name': forms.TextInput(attrs=attrs),
            'email': forms.EmailInput(attrs=attrs),
        }
