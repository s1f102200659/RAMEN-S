from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.account_view, name='account_view'),
]