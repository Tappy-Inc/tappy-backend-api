from django.contrib import admin
from domain.mailer.models.Template import Template
from unfold.admin import ModelAdmin

# Register your models here.

@admin.register(Template)
class TemplateAdmin(ModelAdmin):
    list_display = ('id', 'name', 'subject',)
    search_fields = ('name',)