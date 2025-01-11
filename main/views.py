from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse
import requests
from articles.models import Article
from services.models import Service
from towers.models import Crane
from parts.models import Part


# Create your views here.
def index(request):
    cranes = Crane.objects.filter(is_active=True, is_featered=True).order_by('-id')[:6]
    parts = Part.objects.filter(is_active=True, is_featered=True).order_by('-id')[:6]
    services = Service.objects.filter(is_active=True, is_featured=True).order_by('-id')[:5]
    articles = Article.objects.filter(is_active=True, is_featured=True).order_by('-id')[:6]
    return render(request, 'main/index.html', context={
        'cranes': cranes,
        'parts': parts,
        'services': services,
        'articles': articles,
        'title': 'Главная страница'
    })

def about(request):
    return render(request, 'main/about.html', context={
        'title': 'О компании'
    })

def contact(request):
    return render(request, 'main/contacts.html', context={
        'title': 'Контакты'
    })

@csrf_exempt
def submit_request(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("first-name")
        last_name = request.POST.get("last-name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")

        # Проверка данных
        if not name or not phone:
            return JsonResponse({"error": "Все поля обязательны для заполнения!"}, status=400)

        # Отправка сообщения в Telegram
        bot_token = settings.TELEGRAM_BOT_TOKEN
        chat_id = settings.TELEGRAM_CHAT_ID
        message = f"💡 Заявка на обратную связь:\n\nИмя: {name + ' ' + last_name}\nEmail: {email}\nТелефон: {phone}"

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