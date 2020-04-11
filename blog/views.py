from django.shortcuts import render

from .models import BLOG

# Create your views here.

def Blog(request):
    blogs=BLOG.objects
    return render(request,'myblog.html',{'blogs':blogs})
