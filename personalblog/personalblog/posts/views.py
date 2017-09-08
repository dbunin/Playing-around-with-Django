from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    posts = Post.objects.order_by('pubDate')
    return render(request, 'posts/home.html', {'posts': posts})


def postDetails(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})
