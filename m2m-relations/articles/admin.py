from django.contrib import admin

from .models import Article


class TagPositionInline(admin.TabularInline):
    model = Article
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['published_at']

