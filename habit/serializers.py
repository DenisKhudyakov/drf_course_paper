from rest_framework import serializers

from habit.models import Habit
from habit.validators import (DurationValidator, PeriodicityValidator,
                              PleasantHabitValidator,
                              RelatedHabitIsPleasantValidator,
                              RelatedHabitOrRewardValidator)


class HabitSerializer(serializers.ModelSerializer):
    """Класс сериализатор для Habit"""

    class Meta:
        model = Habit
        fields = [
            "id",
            "creator",
            "place",
            "time",
            "action",
            "is_pleasant",
            "related_habit",
            "periodicity",
            "reward",
            "duration",
            "is_public",
        ]

    def validate(self, data):
        RelatedHabitOrRewardValidator()(data)
        DurationValidator()(data)
        RelatedHabitIsPleasantValidator()(data)
        PleasantHabitValidator()(data)
        PeriodicityValidator()(data)
        return data
