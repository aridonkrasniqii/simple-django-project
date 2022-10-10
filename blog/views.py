from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.contrib.auth.models import User

posts = [

    {
        'author':'CoreyMS',
        'title': 'Blog Post 1',
        'content' : 'First post content',
        'date_posted':'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    posts = Post.objects.all()
    for post in posts:
        user = post.author
        user.username = 'Aridon'
        post.author = user

    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    post = Post.objects.get(id=1)
    username = post.author.username
    return render(request, 'blog/about.html', context= {'username' : username})

def article(request):

    return render(request, 'blog/article.html', context={})
