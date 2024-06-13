from django.urls import path

from habit.apps import HabitConfig
from habit.views import (HabitIsPublicListAPIView, HabitListCreateAPIView,
                         HabitRetriveUpdateDestroyAPIView)

app_name = HabitConfig.name


urlpatterns = [
    path("habits_create/", HabitListCreateAPIView.as_view(), name="habit-create"),
    path("habits/", HabitListCreateAPIView.as_view(), name="habit-list"),
    path(
        "habits_isPublic/", HabitIsPublicListAPIView.as_view(), name="habits-is-public"
    ),
    path(
        "habits/<int:pk>/",
        HabitRetriveUpdateDestroyAPIView.as_view(),
        name="habit-retrieve-update-destroy",
    ),
]
