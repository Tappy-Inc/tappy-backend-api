from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Serializers
from .serializers import ResetPasswordSerializer, ResetPasswordResponseSerializer

# Services
from domain.user.services.user import reset_password, get_user_by_email

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class ResetPasswordAPIView(APIView):

    permission_classes = (AllowAny,)

    @staticmethod
    @swagger_auto_schema(
        operation_description=f"This operation requires {permission_classes} permission",
        request_body=ResetPasswordSerializer,
        responses={
            200: ResetPasswordResponseSerializer()
        },
        operation_id="reset_password",
        tags=["public"],
    )
    def post(request, *args, **kwargs):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        reset_code = serializer.validated_data['reset_code']
        new_password = serializer.validated_data['new_password']

        user = get_user_by_email(email=email)
        if user is None:
            return Response({"message": "User with this email does not exist."}, status=400)

        password_reset = reset_password(user=user, reset_code=reset_code, new_password=new_password)
        logger.info(f"Reset password response: {password_reset}")

        if not password_reset:
            return Response({"message": f"Invalid reset code for email: {email}"}, status=400)

        response_serializer = ResetPasswordResponseSerializer(data={"message": "Password has been reset successfully."})
        response_serializer.is_valid(raise_exception=True)

        return Response(response_serializer.data)
