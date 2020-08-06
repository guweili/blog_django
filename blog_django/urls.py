from django.contrib import admin
from django.urls import re_path, include

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^', include('my_blog.urls')),
    re_path(r'^', include('comment.urls')),
    re_path(r'^', include('user.urls')),
]
