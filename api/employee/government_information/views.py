from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ReadGovernmentInformationSerializer
from domain.user.services.government_information import get_government_information_by_user

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class GovernmentInformationAPIView(APIView):

    permission_classes = (IsAuthenticated,)
    
    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadGovernmentInformationSerializer()
        },
        operation_id="employee_government_information_read",
        tags=["employee.government-information"],
    )
    def get(request):
        government_information = get_government_information_by_user(user=request.user)
        serializer = ReadGovernmentInformationSerializer(government_information)
        return Response(serializer.data)

    # @staticmethod
    # @swagger_auto_schema(
    #     request_body=CreateGovernmentInformationSerializer(),
    #     responses={
    #         200: ReadGovernmentInformationSerializer()
    #     },
    #     operation_id="government_information_create",
    #     tags=["employee"],
    # )
    # def post(request):
    #     serializer = CreateGovernmentInformationSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)
