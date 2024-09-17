from django.shortcuts import render

def account_view(request):
    # 传递动态数据到模板（你可以替换为实际的账户信息）
    context = {
        'account_name': 'サンプル 氏名',
        'account_number': '0000000',
        'balance': '50,000円',
    }
    return render(request, 'account.html', context)