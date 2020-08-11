from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path, include

from blog_django import settings

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^', include('my_blog.urls')),
    re_path(r'^', include('comment.urls')),
    re_path(r'^', include('user.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 没有这一句无法显示上传的图片
