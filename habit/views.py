from rest_framework import generics

from habit.models import Habit
from habit.serializers import HabitSerializer


class HabitListCreateAPIView(generics.ListCreateAPIView):
    """Класс для получения списка и создания нового элемента"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Класс для получения и обновления и удаления элемента"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

