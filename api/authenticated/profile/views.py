from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class UserProfileAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: UserSerializer()
        },
        operation_description=f"This operation requires {permission_classes} permission",
        operation_id="user_profile_read",
        tags=["authenticated"],
    )
    def get(request):
        logger.info(f"authenticated: {request.user}")
        user_serializer = UserSerializer(request.user)
        return Response(user_serializer.data)
