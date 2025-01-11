from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse
import requests
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

@csrf_exempt
def submit_request(request):
    if request.method == "POST":
        # Получение данных из формы
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        crane_name = request.POST.get("crane_name")

        # Проверка данных
        if not name or not phone:
            return JsonResponse({"error": "Все поля обязательны для заполнения!"}, status=400)

        # Отправка сообщения в Telegram
        bot_token = settings.TELEGRAM_BOT_TOKEN
        chat_id = settings.TELEGRAM_CHAT_ID
        message = f"💡 Заявка на уточнение цены:\n\nИмя: {name}\nТелефон: {phone}\nКран: {crane_name}"

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

