from django.urls import path
from .users.views import UsersAPIView
from .users.id.views import UserIdAPIView
from .users.id.profile.views import UserIdProfileAPIView
from .profiles.views import ProfilesAPIView
from .profiles.id.views import ProfileIdAPIView
from .government_informations.views import GovernmentInformationsAPIView


urlpatterns = [
    path('users', UsersAPIView.as_view()),
    path('users/<int:user_id>', UserIdAPIView.as_view()),
    path('users/<int:user_id>/profile', UserIdProfileAPIView.as_view()),
    path('profiles', ProfilesAPIView.as_view()),
    path('profiles/<int:profile_id>', ProfileIdAPIView.as_view()),
    path('government_informations', GovernmentInformationsAPIView.as_view()),
]
