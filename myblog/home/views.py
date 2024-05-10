from django.shortcuts import render
from django.core.paginator import Paginator
from post.models import Post
from .forms import Mesage


def home(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 5)
    posts = paginator.page(1)
    return render(request, 'home.html', context={'posts':posts})

def about(request):
    return render(request, 'resume.html')

def contact(request):
    if request.method == 'post':
        form = Mesage()
    return render(request, 'contact.html')