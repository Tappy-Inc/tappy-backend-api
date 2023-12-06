from django.urls import path
from .genders.views import GendersAPIView
from .departments.views import DepartmentsAPIView
from .departments.id.views import DepartmentsIdAPIView
from .departments.id.job_positions.views import DepartmentsIdJobPositionsAPIView
from .work_setups.views import WorkSetupsAPIView
from .work_setups.id.views import WorkSetupsIdAPIView
from .genders.id.views import GendersIdAPIView
from .job_positions.views import JobPositionsAPIView
from .job_positions.id.views import JobPositionsIdAPIView
from .employment_types.views import EmploymentTypesAPIView
from .employment_types.id.views import EmploymentTypesIdAPIView


urlpatterns = [
    path('genders', GendersAPIView.as_view()),
    path('genders/<int:gender_id>', GendersIdAPIView.as_view()),
    path('departments', DepartmentsAPIView.as_view()),
    path('departments/<int:department_id>', DepartmentsIdAPIView.as_view()),
    path('departments/<int:department_id>/job-positions', DepartmentsIdJobPositionsAPIView.as_view()),
    path('work-setup', WorkSetupsAPIView.as_view()),
    path('work-setup/<int:work_setup_id>', WorkSetupsIdAPIView.as_view()),
    path('job-positions', JobPositionsAPIView.as_view()),
    path('job-positions/<int:job_position_id>', JobPositionsIdAPIView.as_view()),
    path('employment-types', EmploymentTypesAPIView.as_view()),
    path('employment-types/<int:employment_type_id>', EmploymentTypesIdAPIView.as_view()),
]
