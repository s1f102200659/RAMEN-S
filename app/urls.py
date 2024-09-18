from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.home, name='home'),
    path('linked/',views.linked, name='linked'),
    path('check_link/',views.check_link, name='check_link'),
    path('sendmoney/', views.send_money_view, name='send_money'),
    path('friendslist/', views.select_recipient_view, name='friendslist'),
    
    path('billing_history/', views.billing_history, name='billing_history'),
    path('sendfinish/', views.transfer_complete_view, name='sendfinish'),
]