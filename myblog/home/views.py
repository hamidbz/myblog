from django.shortcuts import render
from django.core.paginator import Paginator
from post.models import Post
from .forms import Mesage
from .models import MesageModel


def home(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 5)
    posts = paginator.page(1)
    return render(request, 'home.html', context={'posts':posts})

def about(request):
    return render(request, 'resume.html')

def contact(request):
    if request.method == 'post':
        form = Mesage(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            obj = MesageModel()
            obj.name = form_data.get("name")
            obj.email = form_data.get("email")
            obj.mesg = form_data.get("message")
            obj.save()
    return render(request, 'contact.html')