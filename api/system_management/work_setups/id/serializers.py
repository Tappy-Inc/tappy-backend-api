from rest_framework import serializers

# Models
from domain.system.models import WorkSetup

import logging
logger = logging.getLogger(__name__)


class ReadWorkSetupSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "system_management.work_setups.id.ReadWorkSetupSerializer"
        model = WorkSetup
        fields = [
            'id',
            'work_setup',
            'created_at',
            'updated_at'
        ]


class UpdateWorkSetupSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "system_management.work_setups.id.UpdateWorkSetupSerializer"
        model = WorkSetup
        fields = [
            'work_setup',
        ]


class DeleteWorkSetupSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "system_management.work_setups.id.DeleteWorkSetupSerializer"

    operation = serializers.CharField(max_length=100)
    domain = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=100)
    data = ReadWorkSetupSerializer()
