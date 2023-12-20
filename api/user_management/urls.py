from django.urls import path
from .users.views import UsersAPIView
from .users.id.views import UserIdAPIView
from .users.id.profile.views import UserIdProfileAPIView
from .profiles.views import ProfilesAPIView
from .profiles.id.views import ProfileIdAPIView
from .government_informations.views import GovernmentInformationsAPIView
from .government_informations.id.views import GovernmentInformationIdAPIView
from .work_informations.views import WorkInformationsAPIView
from .work_informations.id.views import WorkInformationIdAPIView
from .educational_backgrounds.views import EducationalBackgroundsAPIView
from .educational_backgrounds.id.views import EducationalBackgroundIdAPIView

urlpatterns = [
    path('users', UsersAPIView.as_view()),
    path('users/<int:user_id>', UserIdAPIView.as_view()),
    path('users/<int:user_id>/profile', UserIdProfileAPIView.as_view()),
    path('profiles', ProfilesAPIView.as_view()),
    path('profiles/<int:profile_id>', ProfileIdAPIView.as_view()),
    path('government-informations', GovernmentInformationsAPIView.as_view()),
    path('government-informations/<int:government_information_id>', GovernmentInformationIdAPIView.as_view()),
    path('work-informations', WorkInformationsAPIView.as_view()),
    path('work-informations/<int:work_information_id>', WorkInformationIdAPIView.as_view()),
    path('educational-backgrounds', EducationalBackgroundsAPIView.as_view()),
    path('educational-backgrounds/<int:educational_background_id>', EducationalBackgroundIdAPIView.as_view()),
]
