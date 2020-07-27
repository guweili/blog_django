#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :expand.py
# @Time      :2020/7/24 15:23
# @Author    :wlgu
from django.core.paginator import Paginator

from blog_django.settings import EACH_PAGE_BLOGS_NUMBER
from my_blog.models import BlogType


def paging(blogs, page, size=EACH_PAGE_BLOGS_NUMBER):
    paginator = Paginator(blogs, size)  # django分页，第一个传入queryset对象，第二个是每页多少个
    page_fo_blogs = paginator.get_page(page)  # 获取当前页码,所对应的queryset对象
    # page_range = list(range(max(page_fo_blogs.number - 2, 1), min(page_fo_blogs.number + 3, paginator.num_pages + 1)))
    page_range = [x for x in range(int(page_fo_blogs.number) - 2, int(page_fo_blogs.number) + 3) if
                  0 < x <= paginator.num_pages]

    # 给页码前后加上省略号
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    # 加上首页尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    blogs_type = BlogType.objects.all()

    context = {
        'blogs_type': blogs_type,
        'page_fo_blogs': page_fo_blogs,
        'page_range': page_range,
    }

    return context
