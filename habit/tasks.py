from celery import shared_task
from django.utils import timezone
from habit.models import Habit
from django.conf import settings
from telegram import Bot


@shared_task
def my_task():
    now = timezone.now()
    habits = Habit.objects.fillter(time=now.time())
    bot = Bot(token=settings.TELEGRAM_TOKEN)

    for habit in habits:
        message = f"Напоминание {habit.action} в {habit.time}"
        if habit.creator.telegram_id:
            bot.send_message(chat_id=habit.creator.telegram_id, text=message)
