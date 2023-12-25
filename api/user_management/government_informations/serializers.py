from rest_framework import serializers

# Models
from domain.user.models import GovernmentInformation

import logging
logger = logging.getLogger(__name__)


class ReadGovernmentInformationSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "user-management.government-informations.ReadGovernmentInformationSerializer"
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


class CreateGovernmentInformationSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "user-management.government-informations.CreateGovernmentInformationSerializer"
        model = GovernmentInformation
        fields = [
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


class PaginateReadGovernmentInformationSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user-management.government-informations.PaginateReadGovernmentInformationSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadGovernmentInformationSerializer(many=True)


class PaginateQueryReadGovernmentInformationSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user-management.government-informations.PaginateQueryReadGovernmentInformationSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")
