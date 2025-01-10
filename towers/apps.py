from django.apps import AppConfig


class TowersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'towers'
    # Переопределенное название приложения
    verbose_name = 'Продукция'
