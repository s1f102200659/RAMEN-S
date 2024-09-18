from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/<int:user_id>/',views.home, name='home'),
    path('request/<int:user_id>/',views.request, name='request'),
    path('linked/',views.linked, name='linked'),
    path('check_link/',views.check_link, name='check_link'),
    path('sendmoney/<int:user_id>/', views.send_money_view, name='sendmoney'),
    path('friendslist/', views.select_recipient_view, name='friendslist'),
    path('billing_history/<int:user_id>/', views.billing_history, name='billing_history'),
    path('sendfinish/', views.transfer_complete_view, name='sendfinish'),
]
