from django.urls import path
from .genders.views import GendersAPIView
from .departments.views import DepartmentsAPIView

urlpatterns = [
    path('genders', GendersAPIView.as_view()),
    path('departments', DepartmentsAPIView.as_view()),
]
