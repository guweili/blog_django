from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect, render

from django.urls import reverse

from comment.models import Comment
from comment.forms import CommentFrom


def submit_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    comment_form = CommentFrom(request.POST, user=request.user)
    if comment_form.is_valid():
        comment = Comment()
        comment.text = comment_form.cleaned_data['text']
        comment.user = comment_form.cleaned_data['user']
        comment.content_object = comment_form.cleaned_data['model_obj']
        comment.object_id = comment_form.cleaned_data['object_id']
        comment.save()

        return redirect(referer)
