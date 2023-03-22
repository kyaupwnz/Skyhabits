from datetime import datetime, timedelta

from celery import shared_task

from habits.models import Habits
from habits.telegram_bot import send_telegram


@shared_task
def check_time():
    time_now = datetime.now()
    start_time = datetime.now() - timedelta(minutes=1)
    habits = Habits.objects.filter(time__gte=start_time)
    for habit in habits.filter(time__lte=time_now):
        if habit.last_time_executed:
            time_send = habit.last_time_executed + timedelta(days=habit.periodicity)
            if time_send == time_now.date():
                send_telegram(habit)
                habit.last_time_executed = time_now.date()
                habit.save()
        else:
            send_telegram(habit)
            habit.last_time_executed = time_now.date()
            habit.save()
