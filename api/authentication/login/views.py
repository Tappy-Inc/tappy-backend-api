from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

# Serializers
from .serializers import LoginSerializer, ReadCredentialSerializer, ErrorDetailSerializer

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class AuthenticationLoginAPIView(APIView):

    @staticmethod
    @swagger_auto_schema(
        request_body=LoginSerializer,
        operation_description="Get tokens for user",
        operation_id="login",
        tags=["authentication"],
        responses={
            200: ReadCredentialSerializer,
            401: ErrorDetailSerializer
        }
    )
    def post(request):
        login_serializer = LoginSerializer(data=request.data)
        login_serializer.is_valid(raise_exception=True)
        user = authenticate(username=login_serializer.validated_data['username'], password=login_serializer.validated_data['password'])
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),  
                'user': user
            }
            # NOTE: Do not use data=data if mixing with Model Serializers
            credential_serializer = ReadCredentialSerializer(data)
            return Response(credential_serializer.data)
        else:
            error_serializer = ErrorDetailSerializer(data={'detail': 'No active account found with the given credentials'})
            error_serializer.is_valid(raise_exception=True)
            return Response(error_serializer.validated_data, status=401)
