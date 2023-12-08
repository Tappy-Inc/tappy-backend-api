from django.contrib import admin
from domain.authentication.models.Session import Session
from unfold.admin import ModelAdmin

# Register your models here.

@admin.register(Session)
class SessionAdmin(ModelAdmin):
    list_display = ('id', 'user', 'session_key', 'session_data', 'expire_date')
    search_fields = ('user', 'session_key',)
