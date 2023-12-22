from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ChangePasswordSerializer, ChangePasswordResponseSerializer
from domain.user.services.user import change_password

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class ChangePasswordAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        operation_description="description",
        operation_id="change_password",
        tags=["authenticated.change-password"],
        request_body=ChangePasswordSerializer,
        responses={
            200: ChangePasswordResponseSerializer()
        }
    )
    def put(request):
        logger.info(f"authenticated: {request.user}")

        password_serializer = ChangePasswordSerializer(data=request.data)
        password_serializer.is_valid(raise_exception=True)

        if not request.user.check_password(password_serializer.validated_data.get('existing_password')):
            return Response({'message': 'Existing password is incorrect.'}, status=400)
        
        if password_serializer.validated_data.get('existing_password') == password_serializer.validated_data.get('new_password'):
            return Response({'message': 'New password cannot be the same as the existing password.'}, status=400)

        change_password(
            request.user,
            password_serializer.validated_data.get('new_password')
        )
        response = {'message': 'Password has been updated.'}
        response_serializer = ChangePasswordResponseSerializer(response)
        return Response(response_serializer.data)
