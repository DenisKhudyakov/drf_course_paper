from django.db import models

from config.settings import AUTH_USER_MODEL, NULLABLE


class Habit(models.Model):
    """Класс модели привычки"""

    creator = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Создатель"
    )
    place = models.CharField(
        max_length=50, verbose_name="Место", **NULLABLE
    )  # Место в котором он создан
    time = models.TimeField(
        verbose_name="Время"
    )  # Время, когда нужно выполнять привычку
    action = models.CharField(
        max_length=50, verbose_name="Действие"
    )  # Действие привычки, которое нужно выполнить
    is_pleasant = models.BooleanField(
        default=False, verbose_name="Хорошая привычка"
    )  # Хорошая привычка
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="Родительская привычка",
        **NULLABLE,
        related_name="related_to_habit",
    )  # Родительская привычка
    periodicity = models.IntegerField(
        default=1, verbose_name="Периодичность"
    )  # Периодичность привычки
    reward = models.CharField(max_length=50, verbose_name="Бонус", **NULLABLE)
    duration = models.DurationField(
        default=None, verbose_name="Продолжительность", **NULLABLE
    )  # Продолжительность привычки
    is_public = models.BooleanField(
        default=False, verbose_name="Публичная привычка"
    )  # Публичная привычка

    def __str__(self) -> str:
        """Строковое представление модели"""
        return f"Я буду {self.action} в {self.time} в {self.place} "

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
