from django.http import HttpResponse

from my_blog.models import Article


def article_detail(request, article_id):
    article_obj = Article.objects.get(id=article_id)
    return HttpResponse(f'文章标题: {article_obj.title}')
