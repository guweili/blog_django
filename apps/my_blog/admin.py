from django.contrib import admin

from my_blog.models import BlogType, Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'update_time', 'author', 'read_num', 'is_delete']
    ordering = ['-created_time']


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name']
