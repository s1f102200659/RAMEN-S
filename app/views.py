from django.http import HttpResponse
from django.shortcuts import render
from .models import Invoice, Payment, User

def index(request):
    return HttpResponse("Hello, Django!")

def home(request):
    return render(request, 'app/home.html')

def request(request):
    return render(request, 'app/request.html')

def linked(request):
    return render(request, 'app/linked.html')
  
from .models import Invoice, Payment, User

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
            'date': invoice.date,
            'amount': invoice.amount,
            'message': invoice.message,
            'paid_users': paid_users
        })
    
    return render(request, 'app/billing_history.html', {'bills': bills})

def check_link(request):
    return render(request, 'app/check_link.html')

def send_money_view(request):
    return render(request, 'app/sendmoney.html')

def select_recipient_view(request):
    return render(request, 'app/friendslist.html')

def transfer_complete_view(request):
    return render(request, 'app/sendfinish.html')

