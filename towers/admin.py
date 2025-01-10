from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline
from .models import Brand, Crane, SEO


class SeoCraneInline(admin.TabularInline):
    model = SEO
    extra = 1
    verbose_name = "Настройка СЕО"
    verbose_name_plural = "Настройки СЕО"

# Register your models here.
@admin.register(Brand)
class BrandAdmin(ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Crane)
class CraneAdmin(ModelAdmin):
    list_display = ('name', 'brand', 'is_active', 'is_featered')
    list_filter = ('is_active', 'is_featered')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SeoCraneInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "brand":
            kwargs["queryset"] = Brand.objects.filter(is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)