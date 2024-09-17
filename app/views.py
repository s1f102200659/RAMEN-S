from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, Django!")

def home(request):
    return render(request, 'app/home.html')

def check_link(request):
    return render(request, 'app/check_link.html')