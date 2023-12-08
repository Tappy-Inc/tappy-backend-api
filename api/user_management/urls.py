from django.urls import path
from .users.views import UsersAPIView
from .users.id.views import UserIdAPIView
from .users.id.profile.views import UserIdProfileAPIView


urlpatterns = [
    path('users', UsersAPIView.as_view()),
    path('users/<int:user_id>', UserIdAPIView.as_view()),
    path('users/<int:user_id>/profile', UserIdProfileAPIView.as_view()),
]
