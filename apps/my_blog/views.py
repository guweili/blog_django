from django.http import HttpResponse
from django.shortcuts import render_to_response

from my_blog.models import Article


def article_detail(request, article_id):
    article_obj = Article.objects.get(id=article_id)
    return HttpResponse(f'文章标题: {article_obj.title}')


def article_list(request):
    articles = Article.objects.filter(is_delete=False)

    return render_to_response('article_list.html', context={'articles': articles})  # 模板渲染
