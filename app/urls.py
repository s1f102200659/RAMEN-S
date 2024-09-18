from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.home, name='home'),
    path('sendmoney/', views.send_money_view, name='send_money'),
    path('friendslist/', views.select_recipient_view, name='friendslist'),
    path('sendfinish/', views.transfer_complete_view, name='sendfinish'),
]