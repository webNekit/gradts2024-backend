from django.urls import path
from . import views

app_name = 'parts'

urlpatterns = [
    path('submit-request/', views.submit_request, name='submit_request'),
    path('', views.index, name='index'),
    path('<slug:slug>/', views.detail, name='detail'),
]