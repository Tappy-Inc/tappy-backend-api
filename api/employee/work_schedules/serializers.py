from rest_framework import serializers

# Models
from domain.user.models import WorkSchedule

import logging
logger = logging.getLogger(__name__)


class ReadWorkScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "employee.work-schedules.ReadWorkScheduleSerializer"
        model = WorkSchedule
        fields = [
            'id',
            'user',
            'day_of_week',
            'shift_start',
            'shift_end',
            'is_rest_day'
        ]
