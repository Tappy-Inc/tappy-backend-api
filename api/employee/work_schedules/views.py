from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Permissions
from domain.user.permissions.groups import IsEmployee

# Serializers
from .serializers import ReadWorkScheduleSerializer

# Services
from domain.user.services.work_schedule import get_work_schedule_by_user

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class WorkScheduleAPIView(APIView):

    permission_classes = (IsEmployee,)
    
    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadWorkScheduleSerializer(many=True)
        },
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="employee_work_schedule_read",
        tags=["employee.work-schedules"],
    )
    def get(request):
        work_schedules =get_work_schedule_by_user(user=request.user)
        serializer = ReadWorkScheduleSerializer(work_schedules, many=True)
        return Response(serializer.data)
