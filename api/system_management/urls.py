from django.urls import path
from .genders.views import GendersAPIView

urlpatterns = [
    path('genders', GendersAPIView.as_view()),
]
