from django.urls import path

from articles import admin
from articles.views import articles_list

urlpatterns = [
    path('', articles_list, name='articles'),
    path('admin/', admin.ArticleAdmin, name='ModelAdmin')
]
