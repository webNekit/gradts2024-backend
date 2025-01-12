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

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название Категории", unique=True)
    slug = models.SlugField(max_length=255, verbose_name="Слан", help_text="человекопонятный URL", unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Активность")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Part(models.Model):
    STATE_OPTIONS = [
        ('new', 'Новый'),
        ('used', 'Бывший в эксплуатации'),
    ]
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Совместимость", help_text="Выберите бренд для совместимости")
    image = models.ImageField(upload_to="products/parts/", verbose_name="Изображение", help_text="Загрузите изображение", blank=True, null=True)
    name = models.CharField(max_length=255, blank=False, verbose_name="Название запасной части")
    slug = models.SlugField(max_length=255, verbose_name="Слан", help_text="человекопонятный URL", unique=True)
    small_text = models.TextField(blank=False, verbose_name="Краткое описание")
    state = models.CharField(max_length=255, choices=STATE_OPTIONS, default='new', verbose_name="Состояние", help_text='Выберите состояние')
    sku = models.CharField(max_length=255, verbose_name="Артикул", help_text="Укажите артикул запасной части")
    is_active = models.BooleanField(default=True, verbose_name="Активность", help_text="Отображать на сайте")
    in_stock = models.BooleanField(default=True, verbose_name="В наличии")
    is_featered = models.BooleanField(default=False, verbose_name="Рекомендуемый", help_text="Отображать на главной странице")

    class Meta:
        verbose_name = "Запасная часть"
        verbose_name_plural = "Запасные части"

    def __str__(self):
        return self.name

class SEO(models.Model):
    part = models.OneToOneField(Part, on_delete=models.CASCADE, verbose_name="Настройка СЕО")
    meta_title = models.CharField(max_length=255, verbose_name="Мета-заголовок", blank=True, null=True)
    meta_description = models.TextField(verbose_name="Мета-описание", blank=True, null=True)
    meta_keywords = models.TextField(verbose_name="Мета-ключевые слова", blank=True, null=True)

    def __str__(self):
        return f"Настройка СЕО для {self.part.name}"