from rest_framework import serializers

from habit.models import Habit
from habit.validators import HabitValidator


class HabitSerializer(serializers.ModelSerializer):
    """Habit serializer"""
    class Meta:
        model = Habit
        fields = (
            'name',
            'place',
            'time',
            'action',
            'is_nice',
            'related',
            'period',
            'reward',
            'time_to_complete',
            'is_public'
        )
        validators = [HabitValidator()]
