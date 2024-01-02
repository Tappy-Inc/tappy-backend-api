from django_filters import rest_framework as filters
from domain.user.models import User


class UserFilter(filters.FilterSet):

    # User Model
    username = filters.CharFilter(lookup_expr='icontains')
    email = filters.CharFilter(lookup_expr='icontains')
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    middle_name = filters.CharFilter(lookup_expr='icontains')

    # Profile Model
    profile__employee_id = filters.CharFilter(field_name='profile__employee_id', lookup_expr='icontains')
    profile__bio = filters.CharFilter(field_name='profile__bio', lookup_expr='icontains')
    profile__location = filters.CharFilter(field_name='profile__location', lookup_expr='icontains')
    profile__gender__gender = filters.CharFilter(field_name='profile__gender__gender', lookup_expr='exact')
    profile__civil_status = filters.CharFilter(field_name='profile__civil_status', lookup_expr='icontains')
    profile__birth_date = filters.DateFilter(field_name='profile__birth_date', lookup_expr='exact')
