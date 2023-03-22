from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models

from users.models import NULLABLE


# Create your models here.
class Habits(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=50, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=100, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Приятная привычка')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL,  verbose_name='Связанная привычка', **NULLABLE)
    periodicity = models.IntegerField(default=1,validators=[MaxValueValidator(7)], verbose_name='Периодичность')
    reward = models.CharField(max_length=150, verbose_name='Вознаграждение', **NULLABLE)
    execution_time = models.IntegerField(default=60, validators=[MaxValueValidator(120)], verbose_name='Время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='Опубликовано')
    last_time_executed = models.DateField(verbose_name='Последнее выполнение', **NULLABLE)

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def __str__(self):
        return f'{self.user} будет {self.action} в {self.place}'
