from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect

from django.urls import reverse

from comment.models import Comment


def submit_comment(request):
    user = request.user
    text = request.POST.get('text', '')

    content_type = request.POST.get('content_type', '')
    obj_id = request.POST.get('obj_id', '')
    model_class = ContentType.objects.get(model=content_type).model_class()
    model_obj = model_class.objects.get(pk=int(obj_id))

    comment = Comment()
    comment.text = text
    comment.user = user
    comment.content_object = model_obj
    comment.object_id = obj_id
    comment.save()

    referer = request.META.get('HTTP_REFERER', reverse('home'))
    return redirect(referer)
