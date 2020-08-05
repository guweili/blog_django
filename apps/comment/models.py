from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.DO_NOTHING,
        verbose_name='用户',
    )
    text = models.TextField(verbose_name='评论内容')

    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, verbose_name='表名')
    object_id = models.PositiveIntegerField(verbose_name='表对应的数据id')
    content_object = GenericForeignKey('content_type', 'object_id')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')

    root = models.ForeignKey('self', null=True, related_name='root_comment', on_delete=models.DO_NOTHING,
                             verbose_name='初始评论id')  # 关联顶级评论
    parent = models.ForeignKey('self', null=True, related_name='parent_comment', on_delete=models.DO_NOTHING,
                               verbose_name='提问id')  # 关联上级评论回复
    reply_to = models.ForeignKey(
        User,
        related_name='replies',
        null=True,
        on_delete=models.DO_NOTHING,
        verbose_name='提问人',
    )  # related_name 重命名反向解析名称

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'comment'
        verbose_name_plural = '评论详情'
        # ordering = ['-created_time']
