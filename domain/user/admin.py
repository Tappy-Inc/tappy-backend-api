from django.contrib import admin

# Register your models here.
from domain.user.models.Document import Document
from domain.user.models.EducationalBackground import EducationalBackground
from domain.user.models.GovernmentInformation import GovernmentInformation
from domain.user.models.Profile import Profile

admin.site.register(Document)
admin.site.register(EducationalBackground)
admin.site.register(GovernmentInformation)
admin.site.register(Profile)
