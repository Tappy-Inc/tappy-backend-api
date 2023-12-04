from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LogoutSerializer, ErrorDetailSerializer
from domain.authentication.services.session import delete_sessions_by_key
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema

class AuthenticationLogoutAPIView(APIView):

    @staticmethod
    @swagger_auto_schema(
        operation_description="Logout user and invalidate session",
        operation_id="logout",
        tags=["authentication"],
        responses={
            200: LogoutSerializer,
            401: ErrorDetailSerializer
        }
    )
    def post(request):
        
        session_key = request.session.session_key

        if session_key is None:
            error_serializer = ErrorDetailSerializer(data={'detail': 'No session key'})
            if error_serializer.is_valid():
                return Response(error_serializer.validated_data, status=401)

        # Delete Session from Database
        delete_sessions_by_key(session_key=session_key)
        
        # Invalidate the session
        request.session.flush()

        logout_serializer = LogoutSerializer(data={'detail': 'Logout successful'})
        if logout_serializer.is_valid():
            response = Response(logout_serializer.validated_data)
            response.delete_cookie(session_key, samesite='none', secure=True)
            return response
