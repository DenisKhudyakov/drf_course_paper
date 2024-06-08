from django.contrib import admin

from habit.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
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
        'is_public',
    )
