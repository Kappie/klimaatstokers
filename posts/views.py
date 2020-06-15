from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Post



def index(request):
    posts = Post.objects.order_by('-pub_date')[:6]
    context = {'posts': posts}
    return render(request, 'posts/index.html', context)

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)
