from django.urls import path
from .genders.views import GendersAPIView
from .departments.views import DepartmentsAPIView
from .departments.id.job_positions.views import DepartmentsIdJobPositionsAPIView
from .work_setup.views import WorkSetupAPIView
from .genders.id.views import GendersIdAPIView


urlpatterns = [
    path('genders', GendersAPIView.as_view()),
    path('genders/<int:gender_id>', GendersIdAPIView.as_view()),
    path('departments', DepartmentsAPIView.as_view()),
    path('departments/<int:department_id>/job-positions', DepartmentsIdJobPositionsAPIView.as_view()),
    path('work-setup', WorkSetupAPIView.as_view()),
]
