from rest_framework import serializers

# Models
from domain.user.models import EducationalBackground

import logging
logger = logging.getLogger(__name__)


class ReadEducationalBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "user-management.educational-backgrounds.ReadEducationalBackgroundSerializer"
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


class CreateEducationalBackgroundSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "user-management.educational-backgrounds.CreateEducationalBackgroundSerializer"
        model = EducationalBackground
        fields = [
            'user',
            'education_type',
            'school',
            'from_year',
            'to_year',
            'degree'
        ]


class PaginateReadEducationalBackgroundSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user-management.educational-backgrounds.PaginateReadEducationalBackgroundSerializer"

    count = serializers.IntegerField()
    next = serializers.URLField()
    previous = serializers.URLField()
    results = ReadEducationalBackgroundSerializer(many=True)


class PaginateQueryReadEducationalBackgroundSerializer(serializers.Serializer): # noqa

    class Meta:
        ref_name = "user-management.educational-backgrounds.PaginateQueryReadEducationalBackgroundSerializer"

    page = serializers.IntegerField(required=False, help_text="A page number within the paginated result set.")
