from .forms import InvoiceCreateForm
from .models import Invoice
from django.http import HttpResponse
from django.shortcuts import render
from .models import Invoice, Payment, User
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

    return render(request, 'app/request.html', context)
def home(request):
    return render(request, 'app/home.html')

def request(request):
    return render(request, 'app/request.html')

def linked(request):
    # デフォルトの請求書IDとユーザーID
    bill_id = 1
    user_id = request.GET.get('user_id')  # クエリパラメータからuser_idを取得

    # 指定された請求書を取得
    invoice = get_object_or_404(Invoice, ID=bill_id)
    
    bill_user = get_object_or_404(User, ID=invoice.user_id)
    bill_user_name = bill_user.name
    bill_user_image = bill_user.image_filename

    # ユーザーが指定されている場合、ユーザーを取得
    user_exists = User.objects.filter(ID=user_id).exists()
    user = get_object_or_404(User, ID=user_id) if user_exists else None

    if request.method == 'POST' and user:
        # 残高が支払い金額以上か確認
        if user.balance >= invoice.amount:
            # 残高を減らす
            user.balance -= invoice.amount
            user.save()

            # 支払い履歴を保存
            Payment.objects.create(
                Invoice_id=invoice,
                Invoice_user_id=user
            )

            # 支払い完了後、メッセージを表示
            return HttpResponse("Success.")
            # return render(request, 'app/home.html')
        else:
            return HttpResponse("Insufficient balance.")
    
    # テンプレートに渡すデータ
    context = {
        'user': user,
        'invoice': invoice,
        'bill_user_name': bill_user_name,
        'user_exists': user_exists,
        'bill_user_image': bill_user_image
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



