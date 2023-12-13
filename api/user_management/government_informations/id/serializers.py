from rest_framework import serializers

# Models
from domain.user.models import GovernmentInformation

import logging
logger = logging.getLogger(__name__)


class ReadGovernmentInformationSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "user_management.government_informations.id.ReadGovernmentInformationSerializer"
        model = GovernmentInformation
        fields = [
            'id',
            'user',
            'sss_no',
            'tin',
            'philhealth',
            'hdmf',
            'prc_license_no',
            'passport_no',
            'tax_status',
            'rdo_number'
        ]


class UpdateGovernmentInformationSerializer(serializers.ModelSerializer):

    # Note: added this field to the serializer to allow for partial updates
    sss_no = serializers.CharField(max_length=30, required=False)
    tin = serializers.CharField(max_length=30, required=False)
    philhealth = serializers.CharField(max_length=30, required=False)
    hdmf = serializers.CharField(max_length=30, required=False)
    prc_license_no = serializers.CharField(max_length=30, required=False)
    passport_no = serializers.CharField(max_length=30, required=False)
    tax_status = serializers.CharField(max_length=30, required=False)
    rdo_number = serializers.CharField(max_length=30, required=False)

    class Meta:
        ref_name = "user_management.government_informations.id.UpdateGovernmentInformationSerializer"
        model = GovernmentInformation
        fields = [
            'sss_no',
            'tin',
            'philhealth',
            'hdmf',
            'prc_license_no',
            'passport_no',
            'tax_status',
            'rdo_number'
        ]


class DeleteGovernmentInformationSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user_management.government_informations.id.DeleteGovernmentInformationSerializer"

    operation = serializers.CharField(max_length=100)
    domain = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=100)
    data = ReadGovernmentInformationSerializer()
