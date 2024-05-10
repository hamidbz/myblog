from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment
from .forms import AddComentForm

def posts(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 1)
    page = request.GET.get('page')
    if page == None:
        page=1
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'posts.html', context={'posts':posts,
                                                'page': page, 
                                                'totalPages':paginator.num_pages})

def details(request, id):
    if request.method == "POST":
        form = AddComentForm(request.POST)
    else:
        form = AddComentForm()
    post = Post.objects.get(id= id)
    coments = Comment.objects.filter(postId=id).values()
    return render(request, 'details.html', context={'post':post, 'coments':coments, 'form':form})

