from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('<slug:slug>/', views.detail, name='detail'),
    path('', views.index, name='index'),
]