from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


from .serializers import ReadUserSerializer
from domain.user.services.user import get_user_by_id

from drf_yasg.utils import swagger_auto_schema

import logging
logger = logging.getLogger(__name__)


class UserIdProfileAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    @staticmethod
    @swagger_auto_schema(
        responses={
            200: ReadUserSerializer()
        },
        operation_id="user_profile.",
        tags=["user-management.users.id.profile"],
    )
    def get(request, user_id):
        logger.info(f"authenticated: {request.user}")
        user = get_user_by_id(user_id)
        user_serializer = ReadUserSerializer(user)
        return Response(user_serializer.data)

