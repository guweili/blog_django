from django.shortcuts import render_to_response, get_object_or_404

from my_blog.models import Blog, BlogType


def home(request):
    return render_to_response('home.html', context={})


def blog_list(request):
    blogs = Blog.objects.all()
    blogs_type = BlogType.objects.all()

    return render_to_response('blog/blog_list.html', context={'blogs': blogs, 'blogs_type': blogs_type})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    return render_to_response('blog/blog_detail.html', context={'blog': blog})


def blogs_with_type(request, blog_type_id):
    blog_type = get_object_or_404(BlogType, id=blog_type_id)
    blogs = Blog.objects.filter(blog_type=blog_type)
    blogs_type = BlogType.objects.all()

    return render_to_response(
        'blog/blog_with_type.html',
        context={
            'blogs': blogs,
            'blogs_type': blogs_type,
            'blog_type': blog_type},
    )
