from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class ReadNumExpand:
    def read_count(self):
        '''
        通过外键反向查询，计数统计
        :return:
        '''
        ct = ContentType.objects.get_for_model(self)
        rd = ReadNum.objects.filter(content_type=ct, object_id=self.id)
        return rd.count()

    def create_read_record(self):
        ct = ContentType.objects.get_for_model(self)
        rd = ReadNum()
        rd.content_type = ct
        rd.object_id = self.id
        rd.save()


class ReadNum(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, verbose_name='表名')
    object_id = models.PositiveIntegerField(verbose_name='表对应的数据id')
    content_object = GenericForeignKey('content_type', 'object_id')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='阅读时间')  # auto_now_add 创建时自动添加时间，后台不能操作子字段

    class Meta:
        db_table = 'read_num'
        verbose_name_plural = '阅读记录'
