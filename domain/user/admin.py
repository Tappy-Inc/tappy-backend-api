from django.contrib import admin

# Register your models here.
from domain.user.models.Document import Document
from domain.user.models.EducationalBackground import EducationalBackground
from domain.user.models.GovernmentInformation import GovernmentInformation
from domain.user.models.Profile import Profile
from domain.user.models.WorkInformation import WorkInformation
from domain.user.models.WorkSchedule import WorkSchedule


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'file_name', 'file_type', 'file_source')
    search_fields = ('file_name',)

@admin.register(EducationalBackground)
class EducationalBackgroundAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'education_type', 'school', 'from_year', 'to_year', 'degree')
    search_fields = ('user', 'school',)

@admin.register(GovernmentInformation)
class GovernmentInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sss_no', 'tin', 'philhealth', 'hdmf', 'prc_license_no', 'passport_no', 'tax_status', 'rdo_number')
    search_fields = ('user',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio', 'location', 'middle_name', 'gender', 'civil_status', 'employee_id', 'birth_date', 'manager')
    search_fields = ('user',)

@admin.register(WorkInformation)
class WorkInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'department', 'job_level')
    search_fields = ('user',)

@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'day_of_week', 'shift_start', 'shift_end', 'is_rest_day')
    search_fields = ('user',)
