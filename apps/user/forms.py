#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :forms.py
# @Time      :2020/7/31 17:17
# @Author    :wlgu

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginFrom(forms.Form):
    username = forms.CharField(label='用户名', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名'}))
    password = forms.CharField(label='密码', required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名密码不正确')
        else:
            self.cleaned_data['user'] = user

        return self.cleaned_data


class RegisterFrom(forms.Form):
    username = forms.CharField(
        label='用户名',
        min_length=3,
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名3-15位'})
    )

    nickname = forms.CharField(
        label='昵称',
        min_length=3,
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入昵称3-15位'})
    )

    email = forms.EmailField(
        label='邮箱',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱'})
    )

    code = forms.CharField(
        label='验证码',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入验证码'})
    )

    password = forms.CharField(
        label='密码',
        min_length=6,
        max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'})
    )

    password_again = forms.CharField(
        label='请再次输入密码',
        min_length=6,
        max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请再次输入密码'})
    )

    def __init__(self, *args, **kwargs):
        if 'request' in kwargs:
            self.request = kwargs.pop('request', None)
        super(RegisterFrom, self).__init__(*args, **kwargs)

    def clean(self):
        session_code = self.request.session.get('email_code', '')
        send_code = self.cleaned_data.get('code', '')
        if not send_code or send_code != session_code:
            raise forms.ValidationError('* 验证码错误')

        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已存在')

        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('邮箱已被使用')

        return email

    def clean_password_again(self):
        password_again = self.cleaned_data['password_again']
        password = self.cleaned_data['password']
        if password_again != password:
            raise forms.ValidationError('两次密码不一致')

        return password_again


class ChangeNicknameForm(forms.Form):
    nickname = forms.CharField(
        label='昵称',
        min_length=3,
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入昵称3-15位'})
    )

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user', None)
        super(ChangeNicknameForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('用户尚未登陆')

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname', '').strip()
        if nickname == '':
            raise forms.ValidationError('名称不能为空')

        return nickname


class BindEmailForm(forms.Form):
    email = forms.EmailField(
        label='邮箱',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱'})
    )

    code = forms.CharField(
        label='验证码',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入验证码'})
    )

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user', None)

        if 'request' in kwargs:
            self.request = kwargs.pop('request', None)
        super(BindEmailForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('用户尚未登陆')

        session_code = self.request.session.get('email_code', '')
        send_code = self.cleaned_data.get('code', '')
        if not send_code or send_code != session_code:
            raise forms.ValidationError('* 验证码错误')

        return self.cleaned_data

    def clean_code(self):
        code = self.cleaned_data.get('code', '').strip()
        if code == '':
            raise forms.ValidationError('验证码不能为空')

        return code

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('邮箱已被使用')

        return email


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label='邮箱',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱'})
    )

    code = forms.CharField(
        label='验证码',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入验证码'})
    )

    password = forms.CharField(
        label='密码',
        min_length=6,
        max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'})
    )

    password_again = forms.CharField(
        label='请再次输入密码',
        min_length=6,
        max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请再次输入密码'})
    )

    def __init__(self, *args, **kwargs):
        if 'request' in kwargs:
            self.request = kwargs.pop('request', None)
        super(ForgotPasswordForm, self).__init__(*args, **kwargs)

    def clean(self):
        session_code = self.request.session.get('email_code', '')
        send_code = self.cleaned_data.get('code', '')
        if not send_code or send_code != session_code:
            raise forms.ValidationError('* 验证码错误')

        return self.cleaned_data

    def clean_password_again(self):
        password_again = self.cleaned_data['password_again']
        password = self.cleaned_data['password']
        if password_again != password:
            raise forms.ValidationError('两次密码不一致')

        return password_again


class ChangePasswordForm(forms.Form):
    password = forms.CharField(
        label='密码',
        min_length=6,
        max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'})
    )

    password_again = forms.CharField(
        label='请再次输入密码',
        min_length=6,
        max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请再次输入密码'})
    )

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user', None)

        if 'request' in kwargs:
            self.request = kwargs.pop('request', None)
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('用户尚未登陆')

        return self.cleaned_data

    def clean_password_again(self):
        password_again = self.cleaned_data['password_again']
        password = self.cleaned_data['password']
        if password_again != password:
            raise forms.ValidationError('两次密码不一致')

        return password_again


class IconForm(forms.Form):
    icon = forms.ImageField(
        label='请选择头像',
    )

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user', None)

        super(IconForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('用户尚未登陆')

        return self.cleaned_data
