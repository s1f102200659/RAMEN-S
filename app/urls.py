from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.account_view, name='account_view'),
    path('sendmoney/', views.send_money_view, name='send_money'),
]