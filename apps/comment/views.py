from django.http import JsonResponse

from comment.models import Comment
from comment.forms import CommentFrom


def submit_comment(request):
    comment_form = CommentFrom(request.POST, user=request.user)
    data = {}
    if comment_form.is_valid():
        comment = Comment()
        comment.text = comment_form.cleaned_data['text']
        comment.user = comment_form.cleaned_data['user']
        comment.content_object = comment_form.cleaned_data['content_obj']
        comment.object_id = comment_form.cleaned_data['object_id']

        parent = comment_form.cleaned_data['parent']
        if parent:
            comment.parent = parent
            comment.root = parent.root if parent.root else parent
            comment.reply_to = parent.user
        comment.save()

        data['status'] = 'SUCCESS'
        data['nickname'] = comment.user.nickname
        data['text'] = comment.text
        data['icon'] = comment.user.icon.url
        data['created_time'] = comment.created_time.strftime('%Y-%m-%d %H:%M:%S')
        data['reply_to'] = comment.reply_to.nickname if parent else ''

        data['id'] = comment.id
        data['root_id'] = comment.root.id if comment.root else None
    else:
        data['status'] = 'ERROR'
        data['message'] = '评论内容不能为空'

    return JsonResponse(data)
