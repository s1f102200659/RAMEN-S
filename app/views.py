from django.http import HttpResponse
from django.shortcuts import render
from app.models import User,Invoice,Payment

def index(request):
    return HttpResponse("Hello, Django!")

def home(request,user_id):
    user = User.objects.get(ID=user_id)
    context = {
        'user': user,
        'user_id': user_id,
    }
    return render(request, 'app/home.html',context)


def request(request,user_id):
    return render(request, 'app/request.html',{'user_id': user_id})

def linked(request):
    return render(request, 'app/linked.html')
  
def billing_history(request,user_id):
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
    return render(request, 'app/billing_history.html', {'bills': bills,'user_id': user_id})

def check_link(request):
    return render(request, 'app/check_link.html')

def send_money_view(request,user_id):
    return render(request, 'app/sendmoney.html', {'user_id': user_id})

def select_recipient_view(request):
    return render(request, 'app/friendslist.html')

def transfer_complete_view(request):
    return render(request, 'app/sendfinish.html')

