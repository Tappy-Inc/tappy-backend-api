from rest_framework import serializers

# Models
from domain.user.models import EducationalBackground

import logging
logger = logging.getLogger(__name__)


class ReadEducationalBackgroundSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "user-management.educational-backgrounds.id.ReadEducationalBackgroundSerializer"
        model = EducationalBackground
        fields = [
            'id',
            'user',
            'education_type',
            'school',
            'from_year',
            'to_year',
            'degree'
        ]


class UpdateEducationalBackgroundSerializer(serializers.ModelSerializer):

    # Note: added this field to the serializer to allow for partial updates
    education_type = serializers.CharField(max_length=255, required=False)
    school = serializers.CharField(max_length=255, required=False)
    from_year = serializers.DateField(required=False)
    to_year = serializers.DateField(required=False)
    degree = serializers.CharField(max_length=255, required=False)

    class Meta:
        ref_name = "user-management.educational-backgrounds.id.UpdateEducationalBackgroundSerializer"
        model = EducationalBackground
        fields = [
            'education_type',
            'school',
            'from_year',
            'to_year',
            'degree'
        ]


class DeleteEducationalBackgroundSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user-management.educational-backgrounds.id.DeleteEducationalBackgroundSerializer"

    operation = serializers.CharField(max_length=100)
    domain = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=100)
    data = ReadEducationalBackgroundSerializer()
