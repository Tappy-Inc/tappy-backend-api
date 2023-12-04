import uuid
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import authenticate

# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

# Serializers
from .serializers import LoginSerializer, ReadCredentialSerializer, ErrorDetailSerializer

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema

# Services
from domain.authentication.services.session import create_session_if_not_exists

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

        if request.session.session_key is None:
            request.session.create()
        session_key = request.session.session_key

        login_serializer = LoginSerializer(data=request.data)
        login_serializer.is_valid(raise_exception=True)
        user = authenticate(username=login_serializer.validated_data['username'], password=login_serializer.validated_data['password'])
        
        if user is not None:
            # Create a session for the user
            session = create_session_if_not_exists(
                user=user,
                session_key=session_key, 
                session_data=str(uuid.uuid4()), 
                expire_date=timezone.now() + timedelta(hours=1)
            )
            # Create tokens for the user
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),  
                'user': user,
            }
            # NOTE: Do not use data=data if mixing with Model Serializers
            credential_serializer = ReadCredentialSerializer(data)
            response = Response(credential_serializer.data)
            # Set the session key in the cookies
            response.set_cookie('sessionid', session_key, samesite='none', secure=True, domain='hris.tappy.com.ph')
            response.set_cookie(session.session_key, session.session_data, samesite='none', secure=True, domain='hris.tappy.com.ph')
            return response
        else:
            error_serializer = ErrorDetailSerializer(data={'detail': 'No active account found with the given credentials'})
            error_serializer.is_valid(raise_exception=True)
            return Response(error_serializer.validated_data, status=401)
