from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название услуги", blank=True)
    description = models.TextField(verbose_name="Описание услуги", blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Активность", help_text="Отображать на сайте")
    is_featured = models.BooleanField(default=False, verbose_name="Рекомендуемый", help_text="Отображать на главной странице")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self) -> str:
        return self.name