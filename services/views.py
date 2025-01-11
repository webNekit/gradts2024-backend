from django.shortcuts import render
from .models import Service

# Create your views here.
def index(request):
    services = Service.objects.filter(is_active=True).order_by('-id')
    return render(request, 'services/index.html', {
        'services': services,
        'title': 'Услуги компании'
    })
