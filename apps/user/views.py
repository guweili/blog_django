from django.contrib import auth
from django.contrib.auth import authenticate, login, get_user_model
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from user.forms import LoginFrom, RegisterFrom, ChangeNicknameForm, BindEmailForm, ForgotPasswordForm, \
    ChangePasswordForm
from utils.expand import random_code

User = get_user_model()


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
        reg_from = RegisterFrom(request.POST, request=request)

        if reg_from.is_valid():
            username = reg_from.cleaned_data['username']
            nickname = reg_from.cleaned_data['nickname']
            email = reg_from.cleaned_data['email']
            password = reg_from.cleaned_data['password']
            # 创建用户
            user = User.objects.create_user(username=username, nickname=nickname, password=password, email=email)
            user.save()
            # 后台记录用户登陆状态
            user = authenticate(username=username, password=password)
            login(request, user)
            del request.session['session']  # 防止一个验证码多次使用

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


def change_nickname(request):
    redirect_to = request.GET.get('from', reverse('home'))
    if request.method == 'POST':
        form = ChangeNicknameForm(request.POST, user=request.user)
        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            user = User.objects.get(username=request.user.username)
            user.nickname = nickname
            user.save()

            return redirect(redirect_to)
    else:
        form = ChangeNicknameForm()

    context = {
        'page_title': '修改昵称',
        'form_title': '修改昵称',
        'submit_text': '修改',
        'form': form,
        'return_back_url': redirect_to,
    }

    return render(request, 'form.html', context=context)


def bind_email(request):
    redirect_to = request.GET.get('from', reverse('home'))
    if request.method == 'POST':
        form = BindEmailForm(request.POST, request=request, user=request.user)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(username=request.user.username)
            user.email = email
            user.save()
            del request.session['email_code']  # 防止一个验证码多次使用

            return redirect(redirect_to)

    else:
        form = BindEmailForm()

    context = {
        'page_title': '绑定邮箱',
        'form_title': '绑定邮箱',
        'submit_text': '绑定',
        'form': form,
        'return_back_url': redirect_to,
    }

    return render(request, 'bind_email.html', context=context)


def forgot_password(request):
    redirect_to = reverse('login')
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST, request=request)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.get(email=email)
            user.set_password(password)
            user.save()
            del request.session['email_code']  # 防止一个验证码多次使用

            return redirect(redirect_to)

    else:
        form = ForgotPasswordForm()

    context = {
        'page_title': '找回密码',
        'form_title': '找回密码',
        'submit_text': '提交',
        'form': form,
        'return_back_url': redirect_to,
    }

    return render(request, 'bind_email.html', context=context)


def change_password(request):
    redirect_to = request.GET.get('from', reverse('home'))
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST, user=request.user)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = User.objects.get(username=request.user.username)
            user.set_password(password)
            user.save()

            return redirect(redirect_to)
    else:
        form = ChangePasswordForm()

    context = {
        'page_title': '修改密码',
        'form_title': '修改密码',
        'submit_text': '修改',
        'form': form,
        'return_back_url': redirect_to,
    }

    return render(request, 'form.html', context=context)


def send_code(request):
    email = request.GET.get('email', reverse('home'))
    if email != '':
        code = random_code()
        request.session['email_code'] = code

        send_mail(
            '绑定邮箱',
            f'验证码: {code}',
            '782178550@qq.com',
            [email],
            fail_silently=False,
        )
        message = 'SUCCESS'
    else:
        message = 'ERROR'

    data = {
        'status': 200,
        'message': message,
    }

    return JsonResponse(data)
