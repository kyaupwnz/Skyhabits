from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from habits.models import Habits


class HabitsValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        related_habit = value.get('related_habit')
        reward = value.get('reward')
        is_pleasant = value.get('is_pleasant')

        if not is_pleasant and related_habit and reward:
            raise serializers.ValidationError('Нельзя одновременно выбрать связанную привычку и указать вознаграждение')
        elif not is_pleasant and not related_habit and not reward:
            raise serializers.ValidationError('Необходимо указать либо связанную привычку, либо вознаграждение')
        elif is_pleasant and any([reward, related_habit]):
            raise serializers.ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class RelatedHabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        related_habit = value.get('related_habit')
        if related_habit:
            obj = get_object_or_404(Habits, pk=related_habit.pk)
            if not obj.is_pleasant:
                raise serializers.ValidationError(
                    'В связанные привычки могут попадать только привычки с признаком приятной привычки')
