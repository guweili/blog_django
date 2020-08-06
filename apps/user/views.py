from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from my_blog.forms import LoginFrom, RegisterFrom


def my_login(request):
    if request.method == 'POST':
        login_from = LoginFrom(request.POST)
        if login_from.is_valid():
            user = login_from.cleaned_data['user']
            login(request, user)  # 后台记录用户登陆状态
            return redirect(request.GET.get('from', reverse('home')))  # 跳回到当前博客
    else:

        login_from = LoginFrom()

    context = {}
    context['login_from'] = login_from

    return render(
        request,
        'login.html',
        context=context
    )


def register(request):
    if request.method == 'POST':
        reg_from = RegisterFrom(request.POST)

        if reg_from.is_valid():
            username = reg_from.cleaned_data['username']
            email = reg_from.cleaned_data['email']
            password = reg_from.cleaned_data['password']
            # 创建用户
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            # 后台记录用户登陆状态
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect(request.GET.get('from', reverse('home')))  # 跳回到当前博客
    else:

        reg_from = RegisterFrom()

    context = {}
    context['reg_from'] = reg_from

    return render(
        request,
        'register.html',
        context=context
    )


def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from', reverse('home')))


def user_info(request):
    return render(request, 'user_info.html')
