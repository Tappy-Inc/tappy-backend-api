from django.urls import path
from .login.views import AuthenticationLoginAPIView
from .session.views import AuthenticationSessionAPIView

# Library: djangorestframework-simplejwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Library: djangorestframework-simplejwt
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', AuthenticationLoginAPIView.as_view()),
    path('session/', AuthenticationSessionAPIView.as_view()),
]
