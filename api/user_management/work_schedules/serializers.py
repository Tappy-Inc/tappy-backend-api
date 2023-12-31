from rest_framework import serializers
from domain.user.models.User import User
from domain.user.models import WorkSchedule


class WorkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "user-management.work-schedules.WorkScheduleSerializer"
        model = WorkSchedule
        fields = ['day_of_week', 'shift_start', 'shift_end', 'is_rest_day']


class CreateWorkScheduleSerializer(serializers.Serializer):

    class Meta:
        ref_name = "user-management.work-schedules.CreateWorkScheduleSerializer"
        
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    schedules = serializers.ListField(child=WorkScheduleSerializer())
