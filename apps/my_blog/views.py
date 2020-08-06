import datetime

from django.shortcuts import get_object_or_404, render
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from my_blog.forms import LoginFrom, RegisterFrom
from my_blog.models import Blog, BlogType
from utils.expand import paging, get_week_data, cache_data


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
    # 添加一条阅读记录
    blog.create_read_record()

    previous_blog = Blog.objects.filter(created_time__lt=blog.created_time).first()  # 上一篇博客
    next_blog = Blog.objects.filter(created_time__gt=blog.created_time).last()  # 下一篇博客

    return render(
        request,
        'blog/blog_detail.html',
        context={
            'blog': blog,
            'previous_blog': previous_blog,
            'next_blog': next_blog,
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
