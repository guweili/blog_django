# Generated by Django 3.0.8 on 2020-07-20 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
            ],
            options={
                'db_table': 'article',
            },
        ),
    ]
