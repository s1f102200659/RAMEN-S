from .forms import InvoiceCreateForm
from .models import Invoice
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

def invoice(request,user_id):
    form = InvoiceCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user_id = request.POST.get('user_id')  # hidden フィールドから取得
        invoice = form.save(commit=False)
        invoice.user_id = user_id
        invoice.save()
        return redirect('check_link')

    context = {
        'form': form,
        'user_id': user_id
    }

    return render(request, 'app/invoice.html', context)

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

def sendfinish_view(request):
    return render(request, 'app/sendfinish.html')

def sendmoney_process(request):
    # if request.method == 'POST':
    #     # 获取表单数据
    #     recipient_name = request.POST.get('recipient_name')
    #     amount = float(request.POST.get('amount'))

    #     # 查找接收送金的用户
    #     recipient = get_object_or_404(User, name=recipient_name)

    #     # 假设有业务逻辑来检查送金金额是否有效（例如：不能超过某个上限）
    #     if amount <= 0 or amount > 50000:
    #         messages.error(request, '送金金額が無効です。')
    #         return redirect('sendmoney')

    #     # 更新接收方用户的余额
    #     recipient.balance += amount
    #     recipient.save()

    #     # 显示成功消息并跳转
    #     messages.success(request, f'{recipient_name} に {amount} 円を送金しました。')
    #     return redirect('sendfinish')

    # 如果不是 POST 请求，则重定向到送金页面
    # return redirect('sendfinish')
    # return redirect('send_money')

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

def transfer_complete_view(request):
    return render(request, 'app/sendfinish.html')
