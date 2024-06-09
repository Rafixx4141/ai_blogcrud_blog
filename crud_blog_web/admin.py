from django.contrib import admin
from .models import Article

# Rejestracja modelu Article za pomocą dekoratora
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'year', 'content', 'image']
    list_display = ['title', 'year']
    list_filter = ['year']
    search_fields = ['title', 'content']