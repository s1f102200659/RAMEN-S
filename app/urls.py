from django.urls import path
from . import views
from .views import top_view

urlpatterns = [
    path('', views.index, name='index'),
    path('top/', top_view, name='top'),
]
