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

    email = forms.EmailField(
        label='邮箱',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱'})
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

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已存在')

        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('邮箱已存在')
        return email

    def clean_password_again(self):
        password_again = self.cleaned_data['password_again']
        password = self.cleaned_data['password']
        if password_again != password:
            raise forms.ValidationError('两次密码不一致')

        return password_again
