from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, Django!")

def home(request):
    return render(request, 'app/home.html')

def linked(request):
    return render(request, 'app/linked.html')
def billing_history(request):
    bills = [
        {'date': '2024-09-01', 'amount': 5000, 'message': 'ランチ代', 'paid_users': [
            {'icon': 'images/human1.png'}
        ]},
        {'date': '2024-09-05', 'amount': 12000, 'message': '飲み会', 'paid_users': [
            {'icon': 'images/human2.png'},
            {'icon': 'images/human3.png'}
        ]}, 
        # 他の請求履歴データ
    ]
    return render(request, 'app/billing_history.html', {'bills': bills})

def check_link(request):
    return render(request, 'app/check_link.html')

def send_money_view(request):
    return render(request, 'sendmoney.html')

def select_recipient_view(request):
    return render(request, 'friendslist.html')

def transfer_complete_view(request):
    return render(request, 'sendfinish.html')

