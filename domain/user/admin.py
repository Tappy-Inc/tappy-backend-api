from django.contrib import admin
# Django: abstract-user
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from domain.user.models.Address import Address
from domain.user.models.Document import Document
from domain.user.models.EducationalBackground import EducationalBackground
from domain.user.models.GovernmentInformation import GovernmentInformation
from domain.user.models.Profile import Profile
from domain.user.models.WorkInformation import WorkInformation
from domain.user.models.WorkSchedule import WorkSchedule

# Library: django-unfold
from domain.user.models.User import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin

from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

# Library: django-unfold
# admin.site.unregister(User) # NOTE: Uncomment this if not using Abstract User
admin.site.unregister(Group)

# Django: abstract-user
fields = list(UserAdmin.fieldsets)
# fields[0] = auth related fields, fields[1] = personal info, fields[2] = permissions, fields[3] = date joined, fields[4] = last login
fields[1] = (None, {'fields': ('first_name', 'last_name', 'middle_name')})
UserAdmin.fieldsets = tuple(fields)

# Library: django-unfold
@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    ordering = ('id',)

# Library: django-unfold
@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

@admin.register(Address)
class AddressAdmin(ModelAdmin):
    list_display = ('id', 'user', 'address', 'address_line_2', 'baranggay', 'city', 'state', 'postal_code', 'country')
    search_fields = ('user', 'city', 'state', 'country',)

@admin.register(EducationalBackground)
class EducationalBackgroundAdmin(ModelAdmin):
    list_display = ('id', 'user', 'education_type', 'school', 'from_year', 'to_year', 'degree')
    search_fields = ('user', 'school',)

@admin.register(Document)
class DocumentAdmin(ModelAdmin):
    list_display = ('id', 'user', 'file_name', 'file_type', 'file_size', 'file_source', 'file_upload')
    search_fields = ('file_name',)

@admin.register(GovernmentInformation)
class GovernmentInformationAdmin(ModelAdmin):
    list_display = ('id', 'user', 'sss_no', 'tin', 'philhealth', 'hdmf', 'prc_license_no', 'passport_no', 'tax_status', 'rdo_number')
    search_fields = ('user',)

@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ('id', 'user', 'get_user_first_name', 'get_user_last_name', 'get_user_email', 'get_bio', 'gender', 'civil_status', 'employee_id', 'birth_date', 'manager')
    search_fields = ('user',)
    list_filter = ('gender', 'civil_status',)

    def get_user_first_name(self, obj):
        return obj.user.first_name
    get_user_first_name.short_description = 'First Name'  # Sets column header

    def get_user_last_name(self, obj):
        return obj.user.last_name
    get_user_last_name.short_description = 'Last Name'  # Sets column header

    def get_user_email(self, obj):
        return obj.user.email
    get_user_email.short_description = 'Email'  # Sets column header

    def get_bio(self, obj):
        return obj.bio[:20] if obj.bio else obj.bio
    get_bio.short_description = 'Bio'  # Sets column header

@admin.register(WorkInformation)
class WorkInformationAdmin(ModelAdmin):
    list_display = ('id', 'user', 'department', 'job_level')
    search_fields = ('user',)

@admin.register(WorkSchedule)
class WorkScheduleAdmin(ModelAdmin):
    list_display = ('id', 'user', 'day_of_week', 'shift_start', 'shift_end', 'is_rest_day')
    search_fields = ('user',)
