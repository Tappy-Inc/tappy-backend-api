from django.contrib import admin
from domain.authentication.models.Session import Session

# Register your models here.

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'session_key', 'session_data', 'expire_date')
    search_fields = ('user', 'session_key',)
