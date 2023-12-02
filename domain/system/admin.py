from django.contrib import admin

# Register your models here.
from domain.system.models.Gender import Gender


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender')
    search_fields = ('gender',)
