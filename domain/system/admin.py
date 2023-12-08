from django.contrib import admin
from domain.system.models.Gender import Gender
from domain.system.models.Department import Department
from domain.system.models.JobLevel import JobLevel
from domain.system.models.WorkSetup import WorkSetup
from domain.system.models.EmploymentType import EmploymentType
from domain.system.models.JobPosition import JobPosition

# Library: django-unfold
from unfold.admin import ModelAdmin

# Register your models here.

@admin.register(Gender)
class GenderAdmin(ModelAdmin):
    list_display = ('id', 'gender')
    search_fields = ('gender',)

@admin.register(Department)
class DepartmentAdmin(ModelAdmin):
    list_display = ('id', 'department_name')
    search_fields = ('department_name',)

@admin.register(JobLevel)
class JobLevelAdmin(ModelAdmin):
    list_display = ('id', 'level')
    search_fields = ('level',)

@admin.register(WorkSetup)
class WorkSetupAdmin(ModelAdmin):
    list_display = ('id', 'work_setup')
    search_fields = ('work_setup',)

@admin.register(EmploymentType)
class EmploymentTypeAdmin(ModelAdmin):
    list_display = ('id', 'employment_type')
    search_fields = ('employment_type',)

@admin.register(JobPosition)
class JobPositionAdmin(ModelAdmin):
    list_display = ('id', 'position_name', 'department')
    search_fields = ('position_name',)