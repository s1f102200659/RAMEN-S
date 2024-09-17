from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, Django!")

def home(request):
    return render(request, 'home.html')

def send_money_view(request):
    return render(request, 'sendmoney.html')

def select_recipient_view(request):
    return render(request, 'friendslist.html')

