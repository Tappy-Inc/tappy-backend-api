from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Serializers
from .serializers import ForgotPasswordSerializer, ForgotPasswordResponseSerializer

# Services
from domain.user.services.user import forgot_password, get_user_by_email

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class ForgotPasswordAPIView(APIView):

    permission_classes = (AllowAny,)

    @staticmethod
    @swagger_auto_schema(
        operation_description=f"This operation requires {permission_classes} permission",
        request_body=ForgotPasswordSerializer,
        responses={
            200: ForgotPasswordResponseSerializer()
        },
        operation_id="forgot_password",
        tags=["public"],
    )
    def post(request, *args, **kwargs):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_user_by_email(email=serializer.validated_data['email'])
        if user is None:
            return Response({"message": "User with this email does not exist."}, status=400)

        forgot_password(user=user)

        response_serializer = ForgotPasswordResponseSerializer(data={"message": "Password reset email has been sent."})
        response_serializer.is_valid(raise_exception=True)

        return Response(response_serializer.data)
