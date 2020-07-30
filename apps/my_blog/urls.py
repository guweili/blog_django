from django.urls import re_path

from my_blog.views import *

urlpatterns = [
    re_path(r'^$', home, name='home'),
    re_path(r'^login/$', my_login, name='login'),
    re_path(r'^blog_list/$', blog_list, name='blog_list'),
    re_path(r'^blog_date/(?P<year>\d+)/(?P<month>\d+)/$', blog_date, name='blog_date'),
    re_path(r'^blog_detail/(?P<blog_id>\d+)/$', blog_detail, name='blog_detail'),
    re_path(r'^blogs_with_type/(?P<blog_type_id>\d+)/$', blogs_with_type, name='blogs_with_type'),
]
