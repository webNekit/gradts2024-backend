from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Service

# Register your models here.
@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ('name', 'is_active', 'is_featured')
    list_filter = ('is_active', 'is_featured')