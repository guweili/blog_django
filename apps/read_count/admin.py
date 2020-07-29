from django.contrib import admin

# Register your models here.
from read_count.models import ReadNum


@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ['content_object', 'content_type', 'object_id', 'created_time']
