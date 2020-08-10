from django.contrib.auth.models import AbstractUser
from django.db import models

status_choices = (
    (0, "不是"),
    (1, "是"),
)


class User(AbstractUser):
    SEX_CHOICES = (
        ('male', '男'),
        ("female", '女'),
    )
    nickname = models.CharField(max_length=30, default='', verbose_name='昵称')
    icon = models.ImageField(upload_to='icon', null=True, blank=True, verbose_name='头像')
    phone = models.IntegerField(null=True, blank=True, verbose_name='电话')
    sex = models.CharField(max_length=30, default="female", choices=SEX_CHOICES, verbose_name='性别')

    class Meta:
        db_table = 'user'
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class UserLoginLog(models.Model):
    '''
    用户登录日志
    '''
    u_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    login_time = models.DateTimeField(blank=True, null=True, verbose_name="登录时间")
    login_ip = models.CharField(null=True, blank=True, max_length=30, verbose_name="登录ip")
    is_delete = models.BigIntegerField(choices=status_choices, default=0, blank=True, null=True, verbose_name="是否删除")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        db_table = 'user_login_log'
        verbose_name = "用户登录日志"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.u_id.nickname
