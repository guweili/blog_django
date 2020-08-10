# Generated by Django 2.2 on 2020-08-10 11:24

import ckeditor_uploader.fields
from django.db import migrations, models
import read_count.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
            options={
                'verbose_name_plural': '博客',
                'db_table': 'blog',
                'ordering': ['-created_time'],
            },
            bases=(models.Model, read_count.models.ReadNumExpand),
        ),
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=30, verbose_name='类型')),
            ],
            options={
                'verbose_name_plural': '博客类型',
                'db_table': 'blog_type',
            },
        ),
    ]
