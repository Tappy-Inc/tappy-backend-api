from django.urls import path
from .government_information.views import GovernmentInformationAPIView
from .work_schedules.views import WorkScheduleAPIView
from .documents.views import DocumentAPIView

urlpatterns = [
    path('government-information', GovernmentInformationAPIView.as_view()),
    path('work-schedules', WorkScheduleAPIView.as_view()),
    path('documents', DocumentAPIView.as_view()),
]
