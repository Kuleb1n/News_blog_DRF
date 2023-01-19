from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'content', 'date_of_publication', 'date_of_change', 'is_published']
    list_display_links = ['id', 'title', 'category']
    list_filter = ['category', 'date_of_publication', 'date_of_change', 'is_published']
    search_fields = ('title', 'content')
    readonly_fields = ('id', 'date_of_publication', 'date_of_change')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']
    list_display_links = ['category_name']
    list_filter = ['category_name']
    search_fields = ('category_name',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
