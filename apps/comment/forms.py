#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :forms.py
# @Time      :2020/7/31 17:17
# @Author    :wlgu

from django import forms
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist
from ckeditor.widgets import CKEditorWidget


class CommentFrom(forms.Form):
    content_type = forms.CharField(
        label='类型id',
        widget=forms.HiddenInput,
    )

    object_id = forms.IntegerField(
        label='文章id',
        required=True,
        widget=forms.HiddenInput,
    )

    text = forms.CharField(
        label=':',
        widget=CKEditorWidget(config_name='comment_ckeditor'),
    )

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user', None)
        super(CommentFrom, self).__init__(*args, **kwargs)

    def clean(self):
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('用户尚未登陆')

        content_type = self.cleaned_data['content_type']
        object_id = self.cleaned_data['object_id']
        try:
            model_class = ContentType.objects.get(model=content_type).model_class()
            model_obj = model_class.objects.get(pk=int(object_id))
            self.cleaned_data['model_obj'] = model_obj
        except ObjectDoesNotExist:
            raise forms.ValidationError('评论对象不存在')

        return self.cleaned_data
