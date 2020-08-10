from django.contrib import admin

# Register your models here.
from read_count.models import ReadNum


@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ['content_object', 'content_type', 'object_id', 'created_time']

    def content_object(self, obj):
        return obj.content_object

    content_object.short_description = '浏览对象'
