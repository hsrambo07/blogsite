from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import operator
from .models import page


def home(request):
    pages=page.objects
    return render(request, 'home.html',{'pages':pages})


def detail(request,blog_id):
    detailblog=get_object_or_404(page, pk=blog_id)
    return render(request,'detail.html',{'pages':detailblog})
