from datetime import datetime

from celery import shared_task

from habit.models import Habit
from habit.services import send_telegram_message


@shared_task
def send_habit_to_telegram():
    """Отправка уведомлений пользователям в telegram"""
    count = 0
    for habit in Habit.objects.filter(is_nice=False):

        if str(datetime.now().time())[:5] == str(habit.time)[:5]:
            message = f'Я буду {habit.action} в {habit.time} в {habit.place}'
            chat_id = habit.owner.chat_id
            send_telegram_message(chat_id=chat_id, text=message)
            count += 1
    return f'send {count} msg'
