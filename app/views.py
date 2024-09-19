from .forms import InvoiceCreateForm
from .models import Invoice
from django.http import HttpResponse
from django.shortcuts import render
from .models import Invoice, Payment, User
from app.models import User,Invoice,Payment
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse

import logging

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
    form = InvoiceCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user_id = request.POST.get('user_id')  # hidden フィールドから取得
        invoice = form.save(commit=False)
        invoice.user_id = user_id
        invoice.save()
        invoice_id = invoice.ID
        
        url = reverse('check_link')
        return redirect(f'{url}?id={invoice_id}&user={user_id}')
    context = {
        'form': form,
        'user_id': user_id
    }

    return render(request, 'app/request.html', context)

def linked(request):
    inv_id = request.GET.get('inv_id')

    if not inv_id:
        return HttpResponse("This link is unavailable.", status=400)

    invoice = get_object_or_404(Invoice, ID=inv_id)
    bill_user = get_object_or_404(User, ID=invoice.user_id)
    # bill_user_balance = bill_user.balance
    # bill_user_name = bill_user.name
    # bill_user_image = bill_user.image_filename

    # 認証されたユーザーをセッションから取得
    user = None
    if request.session.get('user_id'):
        user = get_object_or_404(User, ID=request.session['user_id'])

    if request.method == 'POST':
        button_value = request.POST.get('button')

        if button_value == 'auth':
            user_id = request.POST.get('user_id')
            if user_id:
                user_exists = User.objects.filter(ID=user_id).exists()
                if user_exists:
                    user = get_object_or_404(User, ID=user_id)
                    # セッションにユーザーIDを保存
                    request.session['user_id'] = user_id

            context = {
                'user': user,
                'invoice': invoice,
                'bill_user_name': bill_user.name,
                'bill_user_image': bill_user.image_filename
            }
            return render(request, 'app/linked.html', context)

        elif button_value == 'pay' and user:
            if user.balance >= invoice.amount:
                user.balance -= invoice.amount
                user.save()
                
                bill_user.balance += invoice.amount
                bill_user.save()

                Payment.objects.create(
                    Invoice_id=invoice,
                    Invoice_user_id=user
                )

                # 支払い成功後、セッションからユーザーIDを削除
                # request.session.pop('user_id', None)
                # return render(request, 'app/sendfinish.html', context)
                return HttpResponse("Payment Success.")
            else:
                return HttpResponse("Insufficient balance.")

    context = {
        'user': user,
        'invoice': invoice,
        'bill_user_name': bill_user.name,
        'bill_user_image': bill_user.image_filename
    }
    return render(request, 'app/linked.html', context)

def billing_history(request, user_id):
    # user_idが作成した請求一覧を取得
    invoices = Invoice.objects.filter(user_id=user_id)
    bills = []
    
    for invoice in invoices:
        # 各請求に対して支払ったユーザーの一覧を取得
        payments = Payment.objects.filter(Invoice_id=invoice.ID)
        paid_users = [{'icon': User.objects.get(ID=payment.Invoice_user_id.ID).image_filename} for payment in payments]
        print(paid_users)
        
        bills.append({
            'date': invoice.created_at,
            'amount': invoice.amount,
            'message': invoice.message,
            'paid_users': paid_users
        })
    
    return render(request, 'app/billing_history.html', {'bills': bills})

def check_link(request):
    current_url = request.build_absolute_uri()
    user_id = request.GET.get('user')
    invoice_id = request.GET.get('id')
    if user_id is None:
        return HttpResponse("User ID is missing")
    return render(request, 'app/check_link.html',{'url':current_url,'user_id':user_id,'invoice_id':invoice_id})


def send_money_view(request,user_id):
    return render(request, 'app/sendmoney.html', {'user_id': user_id})

def select_recipient_view(request,user_id):
    return render(request, 'app/friendslist.html', {'user_id': user_id})

def sendfinish_view(request, user_id):
    return render(request, 'app/sendfinish.html', {'user_id': user_id})


def sendfinish_view2(request):
    return render(request, 'app/sendfinish.html')



# def sendmoney_process(request, user_id):
#     # 处理发送逻辑
#     return render(request, 'app/sendfinish.html', {'user_id': user_id})

def sendmoney_process(request, user_id):
    if request.method == 'POST':
        # 获取送金金额
        amount = float(request.POST.get('amount'))
        
        # 获取送金对象（根据 user_id 查询）
        user = get_object_or_404(User, ID=user_id)

        # 检查用户余额是否足够
        if user.balance >= amount:
            # 扣除金额
            user.balance -= amount
            user.save()  # 保存更新后的余额

            # 显示成功信息
            messages.success(request, f'{amount}円が正常に送金されました！')
        else:
            # 余额不足，显示错误信息
            messages.error(request, '残高不足です。')

        # 重定向到某个页面或返回确认页面
        return render(request, 'app/sendfinish.html', {'user_id': user_id})  # 假设你有一个完成页面




