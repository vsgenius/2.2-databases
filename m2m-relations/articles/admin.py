from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                i+=1
        if i == 0:
            raise ValidationError('Укажите основной раздел')
        elif i > 1:
            raise ValidationError('Основным может быть  только один раздел')
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    verbose_name = 'ТЕМАТИКИ СТАТЬИ '
    admin.TabularInline.formset.fields = ArticleScope.tag
    extra = 1
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['published_at']
    inlines = [ArticleScopeInline]


@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ['name']
