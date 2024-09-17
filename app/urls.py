from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.home, name='home'),
    path('sendmoney/', views.send_money_view, name='send_money'),
]