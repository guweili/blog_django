#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :context_processors.py
# @Time      :2020/8/6 19:40
# @Author    :wlgu
from my_blog.forms import LoginFrom


def login_model_form(request):
    return {'login_model_form': LoginFrom()}
