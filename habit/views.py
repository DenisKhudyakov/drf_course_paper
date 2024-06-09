from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, SAFE_METHODS

from habit.models import Habit
from habit.permissions import IsPublic, IsOwner
from habit.serializers import HabitSerializer


class HabitListCreateAPIView(generics.ListCreateAPIView):
    """Класс для получения списка и создания нового элемента"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsPublic]
        elif self.request.method == 'POST':
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class HabitRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Класс для получения и обновления и удаления элемента"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            permission_classes = [IsPublic | IsOwner]
        elif self.request.method in ('PUT', 'PATCH', 'DELETE'):
            permission_classes = [IsAuthenticated | IsOwner]
        return [permission() for permission in permission_classes]


