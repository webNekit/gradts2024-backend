from django.contrib import admin
from .models import Brand, Crane, SEO

# Register your models here.
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Crane)
class CraneAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'is_active', 'is_featered')
    list_filter = ('is_active', 'is_featered')
    prepopulated_fields = {'slug': ('name',)}

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "brand":
            kwargs["queryset"] = Brand.objects.filter(is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)