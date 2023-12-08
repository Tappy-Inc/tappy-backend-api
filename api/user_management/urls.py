from django.urls import path
from .users.views import UsersAPIView
from .users.id.views import UserIdAPIView


urlpatterns = [
    path('users', UsersAPIView.as_view()),
    path('users/<int:user_id>', UserIdAPIView.as_view()),
]
