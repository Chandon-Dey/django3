from django.shortcuts import render
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect 
from .models import Post


# Create your views here.

def blog(request):
    post = Post.objects.all()

    context = {
        'posts':post
    }
    return render(request, 'post/index.html', context)

def blog_details(request, slug):
    post = Post.objects.get(slug=slug)
  

    context = {
       'post':post
    }
    return render(request, 'post/details/details.html', context)