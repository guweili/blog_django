from django.urls import re_path

from user.views import *

urlpatterns = [
    re_path(r'^login/$', my_login, name='login'),
    re_path(r'^logout/$', logout, name='logout'),
    re_path(r'^register/$', register, name='register'),
    re_path(r'^user_info/$', user_info, name='user_info'),
    re_path(r'^change_nickname/$', change_nickname, name='change_nickname'),
    re_path(r'^change_password/$', change_password, name='change_password'),
    re_path(r'^bind_email/$', bind_email, name='bind_email'),
    re_path(r'^send_code/$', send_code, name='send_code'),
    re_path(r'^forgot_password/$', forgot_password, name='forgot_password'),
    re_path(r'^update_icon/$', update_icon, name='update_icon'),
]
