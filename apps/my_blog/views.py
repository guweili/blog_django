from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator  # 分页

from my_blog.models import Blog, BlogType
from utils.expand import paging


def home(request):
    return render_to_response('home.html', context={})


def blog_list(request):
    blogs = Blog.objects.all()
    context = paging(blogs, request)

    return render_to_response(
        'blog/blog_list.html',
        context=context,
    )


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    previous_blog = Blog.objects.filter(created_time__gt=blog.created_time).last()  # 下一篇博客
    next_blog = Blog.objects.filter(created_time__lt=blog.created_time).first()  # 上一篇博客

    return render_to_response(
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

    return render_to_response(
        'blog/blog_with_type.html',
        context=context,
    )


def blog_date(request, year, month):
    blogs = Blog.objects.filter(created_time__year=year, created_time__month=month)
    context = paging(blogs, request)
    context['blog_date'] = f'{year}年 {month}月'

    return render_to_response(
        'blog/blog_date.html',
        context=context,
    )
