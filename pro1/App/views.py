from django.shortcuts import render
from django.http import HttpResponse

def show(request):
    return HttpResponse("<h1>Hello There.....</h1>")

def lili(request):
    return HttpResponse("<h1>Hello Lili 🌼🌼</h1>")

# Create your views here.
