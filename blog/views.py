from django.shortcuts import render
from .models import Blog

def home(request):
    blog=Blog.objects

    return render (request, 'blog/home.html',{'blog':blog})
