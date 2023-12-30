from django.contrib import admin
from domain.mailer.models.Template import Template
from domain.mailer.models.FromEmail import FromEmail
from unfold.admin import ModelAdmin

# Register your models here.

@admin.register(Template)
class TemplateAdmin(ModelAdmin):
    list_display = ('id', 'name', 'subject',)
    search_fields = ('name',)


@admin.register(FromEmail)
class FromEmailAdmin(ModelAdmin):
    list_display = ('id', 'name', 'email',)
    search_fields = ('name', 'email',)
