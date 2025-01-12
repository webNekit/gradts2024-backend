from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline
from .models import Brand, Part, SEO, Category


class SeoPartInline(admin.TabularInline):
    model = SEO
    extra = 1
    verbose_name = "Настройка СЕО"
    verbose_name_plural = "Настройки СЕО"

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
@admin.register(Brand)
class BrandAdmin(ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Part)
class CraneAdmin(ModelAdmin):
    list_display = ('name', 'brand', 'is_active', 'is_featered', 'in_stock')
    list_filter = ('is_active', 'is_featered', 'in_stock')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SeoPartInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "brand":
            kwargs["queryset"] = Brand.objects.filter(is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)