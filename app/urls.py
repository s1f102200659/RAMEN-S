from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.home, name='home'),
    path('check_link/',views.check_link, name='check_link'),
]