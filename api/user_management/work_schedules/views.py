from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Permissions
from domain.user.permissions.groups import IsAdminOrHumanResource

# Serializers
from .serializers import WorkScheduleSerializer, CreateWorkScheduleSerializer

# Services
from domain.user.services.work_schedule import get_work_schedules, create_work_schedule, get_work_schedule_by_user

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class WorkSchedulesAPIView(APIView):

    permission_classes = (IsAdminOrHumanResource,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: WorkScheduleSerializer()
        },
        operation_id="work_schedules_list",
        tags=["user-management.work-schedules"]
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        work_schedules = get_work_schedules()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(work_schedules, request)
        work_schedule_serializer = WorkScheduleSerializer(result_page, many=True)
        return paginator.get_paginated_response(work_schedule_serializer.data)

    @staticmethod
    @swagger_auto_schema(
        request_body=CreateWorkScheduleSerializer,
        operation_description="Create a new work schedule",
        operation_id="work_schedules_create",
        tags=["user-management.work-schedules"],
        responses={
            200: WorkScheduleSerializer()
        }
    )
    def post(request, pk=None, *args, **kwargs):
        logger.info(f"authenticated: {request.user}")
        work_schedule_serializer = CreateWorkScheduleSerializer(data=request.data)
        work_schedule_serializer.is_valid(raise_exception=True)

        logger.info(f"Work Schedule Serializer Data: {work_schedule_serializer.data}")

        for schedule in work_schedule_serializer.validated_data['schedules']:
            work_schedule = create_work_schedule(
                user=work_schedule_serializer.validated_data['user'], 
                day_of_week=schedule['day_of_week'],
                shift_start=schedule['shift_start'],
                shift_end=schedule['shift_end'],
                is_rest_day=schedule['is_rest_day']
            )
        
        work_schedules = get_work_schedule_by_user(work_schedule_serializer.validated_data['user'])
        work_schedule_serializer = WorkScheduleSerializer(work_schedules, many=True)
        return Response(work_schedule_serializer.data)
