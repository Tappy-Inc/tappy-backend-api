from django.utils import timezone

# DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

# Serializers
from .serializers import LoginSerializer, ReadCredentialSerializer, ErrorDetailSerializer

# Library: drf-yasg
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Services
from domain.authentication.services.session import get_session_by_key_and_value

import logging
logger = logging.getLogger(__name__)



class AuthenticationSessionAPIView(APIView):

    @staticmethod
    @swagger_auto_schema(
        operation_description="Validate session cookie",
        operation_id="session",
        tags=["authentication"],
        responses={
            200: ReadCredentialSerializer,
            401: ErrorDetailSerializer
        },
        manual_parameters=[
            openapi.Parameter(
                'session_id', 
                openapi.IN_QUERY, 
                description="Session ID", 
                type=openapi.TYPE_STRING, 
                required=False
            ),
            openapi.Parameter(
                'session_value', 
                openapi.IN_QUERY, 
                description="Session Value", 
                type=openapi.TYPE_STRING, 
                required=False
            )
        ]
    )

    def get(request):
 
        # Get Session ID and Value from Parameter or Cookie
        session_key = request.GET.get('session_id', request.session.session_key)
        session_key_value = request.GET.get('session_value', request.COOKIES.get(session_key))

        if session_key is None:
            error_serializer = ErrorDetailSerializer(data={'detail': 'No session key'})
            if error_serializer.is_valid():
                return Response(error_serializer.validated_data, status=401)

        # Get Session
        session = get_session_by_key_and_value(
            session_key=session_key,
            session_value=session_key_value
        )

        if not session:
            error_serializer = ErrorDetailSerializer(data={'detail': 'Session not found'})
            if error_serializer.is_valid():
                return Response(error_serializer.validated_data, status=401)

        # Expired Session
        if session and session.expire_date < timezone.now():
            error_serializer = ErrorDetailSerializer(data={'detail': 'Session key expired'})
            if error_serializer.is_valid():
                return Response(error_serializer.validated_data, status=401)

        # Generate New Token
        refresh = RefreshToken.for_user(session.user)
        data = {
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),  
            'user': session.user,
        }
        credential_serializer = ReadCredentialSerializer(data)
        response = Response(credential_serializer.data)

        return response
