from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Welcome to Amazon Inventory Management Systems - Home Page </h1>')

def about(request):
    return HttpResponse('<h1> Welcome to Amazon Inventory Management Systems - About Page </h1>')
