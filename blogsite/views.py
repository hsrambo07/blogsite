from django.shortcuts import render
from .models import Blogsite

# Create your views here.

def Blog(request):
    blogsite=Blogsite.objects
    return render(request,'blog.html',{'Blogsite':Blogsite})
    