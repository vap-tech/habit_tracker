from rest_framework.serializers import ValidationError

from habit.models import Habit


class HabitValidator:
    """Habit validator"""

    def __call__(self, habit):
        # Исключить одновременный выбор связанной привычки и указания вознаграждения.
        if all([habit.get('related'), habit.get('reward')]):
            raise ValidationError("Одновременный выбор связанной привычки и указания вознаграждения недопустим.")

        # Время выполнения должно быть не больше 120 секунд.
        if habit.get('time_to_complete'):
            if habit.get('time_to_complete') > 120:
                raise ValidationError("Время выполнения должно быть не больше 120 секунд.")

        # В связанные привычки могут попадать только привычки с признаком приятной привычки.
        if habit.get('related'):
            if not habit.get('related').is_nice:
                raise ValidationError("У связанной привычки отсутствует признак приятной привычки.")

        # У приятной привычки не может быть вознаграждения или связанной привычки.
        if habit.get('is_nice'):
            if any([habit.get('related'), habit.get('reward')]):
                raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")

        # Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
        if habit.get('period'):
            if habit.get('period') > 7:
                raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")
