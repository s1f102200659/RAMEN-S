from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django!")

from django.shortcuts import render

def top_view(request):
    return render(request, 'top.html')