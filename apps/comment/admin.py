from django.contrib import admin

from comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_object', 'content_type', 'text', 'created_time']
    ordering = ['-created_time']

    def content_object(self, obj):
        return obj.content_object

    content_object.short_description = '评论对象'
