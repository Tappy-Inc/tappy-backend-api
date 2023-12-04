from rest_framework import serializers

# Models
from domain.system.models import WorkSetup

import logging
logger = logging.getLogger(__name__)


class ReadWorkSetupSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "system-management.work-setup.ReadWorkSetupSerializer"
        model = WorkSetup
        fields = [
            'id',
            'work_setup',
            'created_at',
            'updated_at'
        ]


class CreateWorkSetupSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "system-management.work-setup.CreateWorkSetupSerializer"
        model = WorkSetup
        fields = [
            'work_setup'
        ]


class PaginateReadWorkSetupSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "system-management.work-setup.PaginateReadWorkSetupSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadWorkSetupSerializer(many=True)


class PaginateQueryReadWorkSetupSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "system-management.work-setup.PaginateQueryReadWorkSetupSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")
