from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('contact-request/', views.submit_request, name='submit_request'),
    path('contacts/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
]