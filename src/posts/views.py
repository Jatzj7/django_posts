from django.shortcuts import render
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    context = {
        'post_list': posts
    }
    return render(request, "post_list.html", context)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {'post': post}
    return render(request, "post_detail.html", context)
