from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, verbose_name="Слан", help_text="человекопонятный URL")
    short_text = models.TextField(verbose_name="Краткое содержание")
    content = RichTextField(verbose_name="Контент статьи", blank=False)
    image = models.ImageField(blank=True, help_text="Загрузите изображение", null=True, upload_to='articles/', verbose_name="Изображение")
    is_active = models.BooleanField(default=True, verbose_name="Отображать на сайте")
    is_featured = models.BooleanField(default=False, verbose_name="Отображать на главной странице")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Статьи и новости"

    def __str__(self):
        return self.title