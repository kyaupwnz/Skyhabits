from rest_framework import serializers

from habits.models import Habits
from habits.validators import HabitsValidator, RelatedHabitValidator


class HabitsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Habits
        fields = '__all__'
        validators = [
            HabitsValidator(field=('related_habit', 'reward', 'is_pleasant')),
            RelatedHabitValidator(field='related_habit')
        ]
