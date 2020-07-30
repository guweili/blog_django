from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='用户'
    )  # DO_NOTHING当用户删除时，对他所作的文章不做任何操作
    text = models.TextField(verbose_name='评论内容')

    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, verbose_name='表名')
    object_id = models.PositiveIntegerField(verbose_name='表对应的数据id')
    content_object = GenericForeignKey('content_type', 'object_id')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')  # auto_now_add 创建时自动添加时间，后台不能操作子字段

    class Meta:
        db_table = 'comment'
        verbose_name_plural = '评论详情'
        ordering = ['-created_time']
