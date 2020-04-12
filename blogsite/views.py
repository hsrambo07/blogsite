from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def blog(request):
    blogs=Blog.objects
    return render(request,'blog.html',{'blogs':blogs})
    

def detail(request,blog_id):
    myblog=Blog.objects
    detailblog=get_object_or_404(Blog, pk=blog_id)
    return render(request,'det.html',{'myblog':detailblog})



    