from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.home, name='home'),
    path('billing_history/', views.billing_history, name='billing_history'),
]