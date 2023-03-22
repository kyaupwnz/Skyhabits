import telebot
from django.conf import settings


def send_telegram(obj):
    bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)
    text = f"Я буду {obj.action} в {obj.time} в {obj.place} и награжу себя  {obj.related_habit or obj.reward}"
    bot.send_message(obj.user.chat_id, text)
