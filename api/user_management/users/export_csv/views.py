import csv

from django.http import HttpResponse
from rest_framework.views import APIView

# Permissions
from domain.user.permissions.groups import IsAdminOrHumanResource

# Serializers
from .serializers import ExportUserSerializer

# Services
from domain.user.services.user import get_users

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)

class UsersExportCSVAPIView(APIView):
    
    permission_classes = (IsAdminOrHumanResource,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: 'CSV file'
        },
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="export-csv",
        tags=["user-management.users"],
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="users.csv"'

        writer = csv.writer(response)
        fields = ExportUserSerializer.Meta.fields
        writer.writerow(fields)

        users = get_users()
        for user in users:
            writer.writerow([getattr(user, field) for field in fields])

        return response
