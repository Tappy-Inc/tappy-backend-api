from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Serializers
from .serializers import ResetPasswordSerializer, ResetPasswordResponseSerializer

# Services
from domain.user.services.user import reset_password, get_user_by_email
from domain.user.caches.email import retrieve_reset_password_otp_code, delete_reset_password_otp_code

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
        otp_code = serializer.validated_data['otp_code']
        new_password = serializer.validated_data['new_password']

        user = get_user_by_email(email=email)
        if user is None:
            return Response({"message": "User with this email does not exist."}, status=400)
        
        reset_password_otp_code = retrieve_reset_password_otp_code(email=email)
        if int(otp_code) != int(reset_password_otp_code):
            return Response({"message": f"Invalid reset otp code for email: {email}"}, status=400)

        password_reset = reset_password(user=user, new_password=new_password)
        delete_reset_password_otp_code(email=email)
        logger.info(f"Reset password response: {password_reset}")

        response_serializer = ResetPasswordResponseSerializer(data={"message": "Password has been reset successfully."})
        response_serializer.is_valid(raise_exception=True)

        return Response(response_serializer.data)
