from django.http import HttpResponse
from django.shortcuts import render 
import operator
from .models import page


def home(request):
    pages=page.objects
    return render(request, 'home.html',{'pages':pages})
