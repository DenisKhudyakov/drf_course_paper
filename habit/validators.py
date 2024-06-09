"""
example code
class EvenNumberValidator:
    def __call__(self, value):
        if value % 2 != 0:
            raise serializers.ValidationError("The value must be an even number.")

class MySerializer(serializers.Serializer):
    number = serializers.IntegerField(validators=[EvenNumberValidator()])
"""

from rest_framework import serializers


class RelatedHabitOrRewardValidator:
    """
    Исключить одновременный выбор связанной привычки и указания вознаграждения.
    В модели не должно быть заполнено одновременно и поле вознаграждения,
    и поле связанной привычки. Можно заполнить только одно из двух полей.
    """

    def __call__(self, habit):
        if habit.reward and habit.related_habit:
            raise serializers.ValidationError(
                "В модели не должно быть заполнено одновременно и поле вознаграждения,"
            )


class DurationValidator:
    """Время выполнения должно быть не больше 120 секунд"""

    def __call__(self, habit):
        if habit.duration and habit.duration > 120:
            raise serializers.ValidationError(
                "Время выполнения должно быть не больше 120 секунд"
            )


class RelatedHabitIsPleasantValidator:
    """В связанные привычки могут попадать только привычки с признаком приятной привычки."""

    def __call__(self, habit):
        if not habit.related_habit.is_pleasant:
            raise serializers.ValidationError(
                "В связанные привычки могут попадать только привычки с признаком приятной привычки."
            )


class PleasantHabitValidator:
    """У приятной привычки не может быть вознаграждения или связанной привычки"""

    def __call__(self, habit):
        if habit.is_pleasant and (habit.related_habit or habit.reward):
            raise serializers.ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки"
            )


class PeriodicityValidator:
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней."""

    def __call__(self, habit):
        if habit.periodicity > 7:
            raise serializers.ValidationError(
                "Нельзя выполнять привычку реже, чем 1 раз в 7 дней."
            )
        if habit.periodicity < 1:
            raise serializers.ValidationError(
                "Нельзя выполнять привычку чаще, чем 1 раз в день."
            )
