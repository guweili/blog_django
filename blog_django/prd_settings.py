#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :prd_settings.py
# @Time      :2020/7/14 11:43
# @Author    :wlgu


from decouple import config  # 将敏感信息保存在特定文件中，和项目隔离开

import dj_database_url  # 将数据库连接的敏感信息隔离开

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': dj_database_url.config(
        default=config('PRD_DATABASE_URL'),
    )
}
