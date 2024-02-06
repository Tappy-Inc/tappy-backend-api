from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Serializers
from .serializers import ValidateOTPResponseSerializer, ValidateOTPSerializer

# Services
from domain.user.services.user import reset_password, get_user_by_email
from domain.user.caches.email import retrieve_reset_password_otp_code, delete_reset_password_otp_code

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class ValidateOTPAPIView(APIView):

    permission_classes = (AllowAny,)

    @staticmethod
    @swagger_auto_schema(
        operation_description=f"This operation requires {permission_classes} permission",
        request_body=ValidateOTPSerializer,
        responses={
            200: ValidateOTPResponseSerializer()
        },
        operation_id="validate_otp",
        tags=["public"],
    )
    def post(request, *args, **kwargs):
        serializer = ValidateOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        otp_code = serializer.validated_data['otp_code']
        
        reset_password_otp_code = retrieve_reset_password_otp_code(email=email)
        
        if reset_password_otp_code is None:
            return Response({"message": f"Invalid reset otp code for email: {email}"}, status=400)

        if int(otp_code) != int(reset_password_otp_code):
            return Response({"message": f"Invalid reset otp code for email: {email}"}, status=400)

        response_serializer = ValidateOTPResponseSerializer(data={"message": "OTP has been validated successfully."})
        response_serializer.is_valid(raise_exception=True)

        return Response(response_serializer.data)
