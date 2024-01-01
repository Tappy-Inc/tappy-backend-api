from rest_framework import serializers

# Models
from domain.user.models.User import User

class ExportUserSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "user-management.users.ExportUserSerializer"
        model = User
        fields = ['id', 'username', 'first_name', 'middle_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined']
