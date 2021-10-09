from django import forms
from django.contrib.auth.hashers import check_password
from django.forms.widgets import PasswordInput

from .models import Dsuser


class RegisterFrom(forms.Form):
    name = forms.CharField(max_length=128, label='아이디', error_messages={
        'required': '모든 값을 입력하여야 합니다.'
    })
    email = forms.EmailField(max_length=128, label='이메일', error_messages={
        'required': '모든 값을 입력해야 합니다.'
    })
    password = forms.CharField(max_length=256, widget=forms.PasswordInput, label='비밀번호', error_messages={
        'required': '모든 값을 입력해야 합니다.'
    })
    re_password = forms.CharField(max_length=256, widget=forms.PasswordInput, label='비밀번호 확인', error_messages={
        'required': '모든 값을 입력해야 합니다.'
    })

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password and password != re_password:
            self.add_error('password', '비밀번호가 다릅니다.')
            self.add_error('re_password', '비밀번호가 다릅니다.')


class LoginForm(forms.Form):
    name = forms.CharField(max_length=128, label='아이디', error_messages={
        'required': '모든 값을 입력하여야 합니다.'
    })
    password = forms.CharField(max_length=256, widget=forms.PasswordInput, label='비밀번호', error_messages={
        'required': '모든 값을 입력해야 합니다.'
    })

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get('name')
        password = cleaned_data.get('password')

        if name and password:
            try:
                user = Dsuser.objects.get(name=name)

                if not check_password(password, user.password):
                    self.add_error('password', '비밀번호가 일치하지 않습니다.')
                    
            except Dsuser.DoesNotExist as e:
                self.add_error('name', '아이디가 없습니다.')
