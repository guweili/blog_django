# Generated by Django 2.2 on 2020-07-22 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章'},
        ),
    ]