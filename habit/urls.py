from django.urls import path

from habit.apps import HabitConfig
from habit.views import (HabitListCreateAPIView,
                         HabitRetriveUpdateDestroyAPIView)

app_name = HabitConfig.name


urlpatterns = [
    path("habits/", HabitListCreateAPIView.as_view(), name="habit-list-create"),
    path(
        "habits/<int:pk>/",
        HabitRetriveUpdateDestroyAPIView.as_view(),
        name="habit-retrieve-update-destroy",
    ),
]
