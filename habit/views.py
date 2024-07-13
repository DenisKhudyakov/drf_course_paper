from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated

from habit.models import Habit
from habit.pagination import CustomPageNumberPagination
from habit.permissions import IsOwner, IsPublic
from habit.serializers import HabitSerializer


class HabitListCreateAPIView(generics.ListCreateAPIView):
    """Класс для получения списка и создания нового элемента"""

    serializer_class = HabitSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            return Habit.objects.filter(user=user)
        return Habit.objects.all()

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated]
        elif self.request.method == "POST":
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]

    def get(self, request, *args, **kwargs):
        queryset = Habit.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = HabitSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class HabitIsPublicListAPIView(generics.ListAPIView):
    """Класс для получения списка элементов, с признаком is_public"""

    serializer_class = HabitSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Класс для получения и обновления и удаления элемента"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [IsPublic | IsOwner]
        elif self.request.method in ("PUT", "PATCH", "DELETE"):
            self.permission_classes = [IsAuthenticated | IsOwner]
        return [permission() for permission in self.permission_classes]
