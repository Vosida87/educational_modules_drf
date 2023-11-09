from django.contrib import admin
from modules.models import EducationalModule


@admin.register(EducationalModule)
class EducationalModuleAdmin(admin.ModelAdmin):
    """Для создания модулей в админке"""
    list_display = ('owner', 'title')
