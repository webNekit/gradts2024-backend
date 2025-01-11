from django.shortcuts import render, get_object_or_404

from towers.models import Crane


# Create your views here.
def index(request):
    cranes = Crane.objects.filter(is_active=True).order_by('-id')
    return render(request, 'towers/index.html', {
        'cranes': cranes,
        'title': 'Продажа башенных кранов'
    })

def detail(request, slug):
    crane = get_object_or_404(Crane, slug=slug, is_active=True)
    seo = crane.seo if crane.seo else None
    return render(request, 'towers/detail.html', {
        'crane': crane,
        'title': crane.name,
        'meta_title': seo.meta_title,
        'meta_description': seo.meta_description,
        'meta_keywords': seo.meta_keywords,
        'meta_image': crane.image.url
    })