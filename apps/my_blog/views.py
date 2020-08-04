import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils import timezone

from comment.models import Comment
from my_blog.forms import LoginFrom, RegisterFrom
from my_blog.models import Blog, BlogType
from utils.expand import paging, get_week_data, cache_data
from comment.forms import CommentFrom


def home(request):
    ct = ContentType.objects.get_for_model(Blog)
    data = get_week_data(ct)

    today = timezone.now().date()

    yesterday = timezone.now().date() - datetime.timedelta(days=1)

    sever_day = timezone.now().date() - datetime.timedelta(days=7)

    return render(
        request,
        'home.html',
        context={
            'data': data,
            'hot_data': cache_data('hot_data', today),
            'yesterday_data': cache_data('yesterday_data', yesterday),
            'sever_day_data': cache_data('sever_day_data', today, sever_day),
        },
    )


def blog_list(request):
    blogs = Blog.objects.all()
    context = paging(blogs, request)

    return render(
        request,
        'blog/blog_list.html',
        context=context,
    )


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog_content_type = ContentType.objects.get_for_model(blog)
    comments = Comment.objects.filter(content_type=blog_content_type, object_id=blog.id)
    # 添加一条阅读记录
    blog.create_read_record()

    previous_blog = Blog.objects.filter(created_time__gt=blog.created_time).last()  # 下一篇博客
    next_blog = Blog.objects.filter(created_time__lt=blog.created_time).first()  # 上一篇博客

    return render(
        request,
        'blog/blog_detail.html',
        context={
            'blog': blog,
            'user': request.user,
            'previous_blog': previous_blog,
            'next_blog': next_blog,
            'comments': comments,
            'comment_from': comments,
        }
    )


def blogs_with_type(request, blog_type_id):
    blog_type = get_object_or_404(BlogType, id=blog_type_id)
    blogs = Blog.objects.filter(blog_type=blog_type)
    context = paging(blogs, request)
    context['blog_type'] = blog_type

    return render(
        request,
        'blog/blog_with_type.html',
        context=context,
    )


def blog_date(request, year, month):
    blogs = Blog.objects.filter(created_time__year=year, created_time__month=month)
    context = paging(blogs, request)
    context['blog_date'] = f'{year}年 {month}月'

    return render(
        request,
        'blog/blog_date.html',
        context=context,
    )


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
