from rest_framework import serializers

# Models
from domain.system.models import CompanyInformation

import logging
logger = logging.getLogger(__name__)


class ReadCompanyInformationSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "system-management.company-informations.id.ReadCompanyInformationSerializer"
        model = CompanyInformation
        fields = [
            'id',
            'company_name',
            'address',
            'number',
            'company_size',
            'industry',
            'created_at',
            'updated_at'
        ]


class UpdateCompanyInformationSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "system-management.company-informations.id.UpdateCompanyInformationSerializer"
        model = CompanyInformation
        fields = [
            'company_name',
            'address',
            'number',
            'company_size',
            'industry',
        ]


class DeleteCompanyInformationSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "system-management.company-informations.id.DeleteCompanyInformationSerializer"

    operation = serializers.CharField(max_length=100)
    domain = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=100)
    data = ReadCompanyInformationSerializer()
