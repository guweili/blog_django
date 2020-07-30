from django.urls import re_path

from comment.views import *

urlpatterns = [
    re_path(r'^comment/$', submit_comment, name='comment'),

]
