from django.core.exceptions import ValidationError
from rest_framework import serializers

from habit.models import Habit
from habit.validators import (DurationValidator, PeriodicityValidator,
                              PleasantHabitValidator,
                              RelatedHabitIsPleasantValidator,
                              RelatedHabitOrRewardValidator)
from users.models import User


class HabitSerializer(serializers.ModelSerializer):
    """Класс сериализатор для Habit"""

    creator = serializers.SlugRelatedField(
        slug_field="email", queryset=User.objects.all()
    )

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

        habit = Habit(**data)

        validators = [
            RelatedHabitOrRewardValidator(),
            DurationValidator(),
            RelatedHabitIsPleasantValidator(),
            PleasantHabitValidator(),
            PeriodicityValidator(),
        ]

        for validator in validators:
            try:
                validator(habit)
            except ValidationError as error:
                raise serializers.ValidationError(error.message)

        return data
