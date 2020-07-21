from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    pass

    def __str__(self):
        return f'{self.title}'

    class Meta:
        db_table = 'article'
        verbose_name = '文章'
