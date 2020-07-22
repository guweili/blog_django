from django.contrib import admin

from my_blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'update_time', 'author', 'read_num', 'is_delete']
    ordering = ['-id']
