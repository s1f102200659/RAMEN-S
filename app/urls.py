from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/<int:user_id>/',views.home, name='home'),
    path('invoice/<int:user_id>/',views.invoice, name='invoice'),
    path('linked/',views.linked, name='linked'),
    path('check_link/',views.check_link, name='check_link'),
    path('sendmoney/<int:user_id>/', views.send_money_view, name='sendmoney'),
    path('friendslist/<int:user_id>/', views.select_recipient_view, name='friendslist'),
    path('billing_history/<int:user_id>/', views.billing_history, name='billing_history'),
    path('sendfinish/<int:user_id>/', views.sendfinish_view, name='sendfinish'),
    path('sendmoney_process/<int:user_id>/', views.sendmoney_process, name='sendmoney_process'),
    path('sendmoney/', views.send_money_view, name='send_money'),
    path('friendslist/', views.select_recipient_view, name='friendslist'),
]