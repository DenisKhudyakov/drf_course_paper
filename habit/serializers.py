from rest_framework import serializers
from habit.models import Habit
from users.models import User


class HabitSerializer(serializers.ModelSerializer):
    """Класс сериализатор для Habit"""
    creator = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Habit
        fields = [
            'id',
            'creator',
            'place',
            'time',
            'action',
            'is_pleasant',
            'related_habit',
            'periodicity',
            'reward',
            'duration',
            'is_public'
        ]