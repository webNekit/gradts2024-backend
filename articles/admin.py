from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Article

@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ('title', 'is_active', 'is_featured')
    list_filter = ('is_active', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}

