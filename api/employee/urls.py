from django.urls import path
from .government_information.views import GovernmentInformationAPIView


urlpatterns = [
    path('government-information', GovernmentInformationAPIView.as_view()),
]
