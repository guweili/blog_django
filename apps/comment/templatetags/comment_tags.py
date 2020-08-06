#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :comment_tags.py
# @Time      :2020/8/6 10:35
# @Author    :wlgu
from django import template
from django.contrib.contenttypes.models import ContentType

from comment.models import Comment

register = template.Library()


@register.simple_tag
def get_comment_count(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return Comment.objects.filter(content_type=content_type, object_id=obj.id).count()
