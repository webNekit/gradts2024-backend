from django.db import models



class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название бренда", unique=True)
    slug = models.SlugField(max_length=255, verbose_name="Слан", help_text="человекопонятный URL", unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Активность")

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    def __str__(self):
        return self.name

class Crane(models.Model):
    STATE_OPTIONS = [
        ('new', 'Новый'),
        ('used', 'Бывший в эксплуатации'),
    ]
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Бренд", help_text="Выберите бренд")
    image = models.ImageField(upload_to="products/towers/", verbose_name="Изображение", help_text="Загрузите изображение", blank=True, null=True)
    name = models.CharField(max_length=255, blank=False, verbose_name="Название крана", help_text="Башенный кран YONGMAO 3100")
    slug = models.SlugField(max_length=255, verbose_name="Слан", help_text="человекопонятный URL", unique=True)
    small_text = models.TextField(blank=False, verbose_name="Краткое описание")
    state = models.CharField(max_length=255, choices=STATE_OPTIONS, default='new', verbose_name="Состояние", help_text='Выберите состояние')
    max_load_capacity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Грузоподъемность макс. (тонн)', help_text='Укажите максимальную грузоподъемность в тоннах')
    max_reach = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Макс. вылет стрелы (м)', help_text='Укажите максимальный вылет стрелы в метрах')
    load_at_max_reach = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Грузоподъемность на макс. вылете (тонн)', help_text='Укажите грузоподъемность на максимальном вылете стрелы в тоннах')
    hook_height = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Высота подъема крюка (м)', help_text='Укажите максимальную высоту подъема крюка в метрах')
    is_active = models.BooleanField(default=True, verbose_name="Активность", help_text="Отображать на сайте")
    is_featered = models.BooleanField(default=False, verbose_name="Рекомендуемый", help_text="Отображать на главной странице")

    class Meta:
        verbose_name = "Башенный кран"
        verbose_name_plural = "Башенные краны"

    def __str__(self):
        return self.name

class SEO(models.Model):
    crane = models.OneToOneField(Crane, on_delete=models.CASCADE, verbose_name="Настройка СЕО")
    meta_title = models.CharField(max_length=255, verbose_name="Мета-заголовок", blank=True, null=True)
    meta_description = models.TextField(verbose_name="Мета-описание", blank=True, null=True)
    meta_keywords = models.TextField(verbose_name="Мета-ключевые слова", blank=True, null=True)

    def __str__(self):
        return f"Настройка СЕО для {self.crane.name}"