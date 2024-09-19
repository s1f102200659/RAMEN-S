from django.http import HttpResponse
from django.shortcuts import render
from app.models import User,Invoice,Payment
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

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

def select_recipient_view(request,user_id):
    return render(request, 'app/friendslist.html', {'user_id': user_id})

def sendfinish_view(request, user_id):
    return render(request, 'app/sendfinish.html', {'user_id': user_id})

def sendfinish_view2(request):
    return render(request, 'app/sendfinish.html')





def sendmoney_process(request, user_id):
    # 处理发送逻辑
    return render(request, 'app/sendfinish.html', {'user_id': user_id})



    try:
        recipient_name = request.POST.get('recipient_name')
        print(1)
        amount = float(request.POST.get('amount'))
        print(2)

        recipient = get_object_or_404(User, name=recipient_name)
        print(3)
        recipient.balance += amount
        print(4)
        recipient.save()
        print(5)
    except Exception as e:
        print(e)
        messages.error(request, '送金金額が無効です。')
        return redirect('send_money')
    finally:
        return redirect('sendfinish')
