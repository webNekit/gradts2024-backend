from unicodedata import category

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse
import requests
from django.core.paginator import Paginator
from parts.models import Part, Category


# Create your views here.
def index(request):
    category_slug = request.GET.get('category', None)
    categories = Category.objects.filter(is_active=True).order_by('-id')

    if category_slug:
        parts = Part.objects.filter(is_active=True, category__slug=category_slug).order_by('-id')
    else:
        parts = Part.objects.filter(is_active=True).order_by('-id')

    paginator = Paginator(parts, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'parts/index.html', {
        'page_obj': page_obj,
        'categories': categories,
        'title': 'Запасные части',
        'selected_category': category_slug,
    })

def detail(request, slug):
    part = get_object_or_404(Part, slug=slug, is_active=True)
    seo = part.seo if part.seo else None
    return render(request, 'parts/detail.html', {
        'part': part,
        'title': part.name,
        'meta_title': seo.meta_title,
        'meta_description': seo.meta_description,
        'meta_keywords': seo.meta_keywords,
        'meta_image': part.image.url
    })

@csrf_exempt
def submit_request(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        part_name = request.POST.get("part_name")

        # Проверка данных
        if not name or not phone:
            return JsonResponse({"error": "Все поля обязательны для заполнения!"}, status=400)

        # Отправка сообщения в Telegram
        bot_token = settings.TELEGRAM_BOT_TOKEN
        chat_id = settings.TELEGRAM_CHAT_ID
        message = f"💡 Заявка на уточнение цены:\n\nИмя: {name}\nТелефон: {phone}\nЗапасная часть: {part_name}"

        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "HTML",
        }

        response = requests.post(url, data=payload)
        if response.status_code == 200:
            return HttpResponse("Ваша заявка успешно отправлена")
        else:
            return JsonResponse({"error": "Не удалось отправить заявку. Попробуйте позже."}, status=500)

    return JsonResponse({"error": "Некорректный запрос."}, status=400)

