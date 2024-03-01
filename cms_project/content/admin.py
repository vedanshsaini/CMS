from django.contrib import admin
from .models import Category, Content

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')
    search_fields = ('title', 'body', 'summary')
    # You can customize other settings such as list_filter, fieldsets, etc.
