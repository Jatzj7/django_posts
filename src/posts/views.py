from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from .forms import postForm
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


def post_create(request):
    form = postForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/posts')

    context = {
        "form": form
    }
    return render(request, "post_create.html", context)
