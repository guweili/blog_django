from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.models import ContentType

from blog_django import settings
from read_count.models import ReadNum, ReadNumExpand


class BlogType(models.Model):
    type_name = models.CharField(max_length=30, verbose_name='类型')

    def blog_count(self):
        '''
        通过外键反向查询，计数统计
        :return:
        '''
        return self.blog_set.count()

    def __str__(self):
        return f'{self.type_name}'

    class Meta:
        db_table = 'blog_type'
        verbose_name_plural = '博客类型'


class Blog(models.Model, ReadNumExpand):
    title = models.CharField(max_length=30, verbose_name='标题')
    content = RichTextUploadingField(verbose_name='内容')  # 富文本
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # auto_now_add 创建时自动添加时间，后台不能操作子字段
    update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')  # auto_now 每次数据有修改时，时间自动更新，后台不能操作子字段
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        verbose_name='作者'
    )  # DO_NOTHING当用户删除时，对他所作的文章不做任何操作
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    blog_type = models.ForeignKey(
        BlogType,
        on_delete=models.DO_NOTHING,
        verbose_name='文章类型'
    )
    read_nums = GenericRelation(ReadNum)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'blog'
        verbose_name_plural = '博客'
        ordering = ['-created_time']
