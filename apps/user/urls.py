from django.urls import re_path

from user.views import *

urlpatterns = [
    re_path(r'^login/$', my_login, name='login'),
    re_path(r'^logout/$', logout, name='logout'),
    re_path(r'^register/$', register, name='register'),
    re_path(r'^user_info/$', user_info, name='user_info'),
]
