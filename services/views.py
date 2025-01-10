from django.shortcuts import render
from .models import Service

# Create your views here.
def collection(request):
    services = Service.objects.filter(is_active=True).order_by('-id')
