from django.urls import re_path

from my_blog.views import *

urlpatterns = [
    re_path(r'^article/(?P<article_id>\d)/$', article_detail, name='article_detail'),
    re_path(r'^article_list/$', article_list, name='article_list'),
]
