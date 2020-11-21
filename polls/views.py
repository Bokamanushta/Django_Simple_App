from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request) : 
    return HttpResponse("Hello, Yeasin. Your are at the polls index. <h3>H1 Heading</h3>")