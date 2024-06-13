from celery import shared_task
from django.conf import settings
from django.utils import timezone
from telegram import Bot

from habit.models import Habit


@shared_task
def send_habit_reminder():
    now = timezone.now()
    habits = Habit.objects.fillter(time=now.time())
    bot = Bot(token=settings.TELEGRAM_TOKEN)

    for habit in habits:
        message = f"Напоминание {habit.action} в {habit.time}"
        if habit.creator.telegram_id:
            bot.send_message(chat_id=habit.creator.telegram_id, text=message)
