from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE


class User(AbstractUser):
    """Класс модели пользователя"""

    phone = models.CharField(
        unique=True, max_length=11, **NULLABLE, verbose_name="Телефон"
    )
    city = models.CharField(max_length=50, **NULLABLE, verbose_name="Город")
    avatar = models.ImageField(
        upload_to="avatars", **NULLABLE, verbose_name="Аватар"
    )  # Сохраняем в папку avatars

    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    telegram_id = models.CharField(
        max_length=50, verbose_name="Telegram_char_id", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
