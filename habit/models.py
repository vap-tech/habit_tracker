from django.db import models

from users.models import NULLABLE, User


class Habit(models.Model):
    """Habit"""
    name = models.CharField(max_length=100, verbose_name='название')
    owner = models.ForeignKey(User, verbose_name='создатель', on_delete=models.CASCADE, **NULLABLE)
    place = models.CharField(max_length=200, verbose_name='место', **NULLABLE)
    time = models.TimeField(verbose_name='время', **NULLABLE)
    action = models.CharField(verbose_name='действие', **NULLABLE)
    is_nice = models.BooleanField(verbose_name='это приятно', **NULLABLE)
    related = models.ForeignKey('self', verbose_name='связанная', on_delete=models.SET_NULL, **NULLABLE)
    period = models.PositiveIntegerField(verbose_name='периодичность', default=1)
    reward = models.CharField(verbose_name='награда', max_length=250, **NULLABLE)
    time_to_complete = models.PositiveIntegerField(verbose_name='время на выполнение', default=45, **NULLABLE)
    is_public = models.BooleanField(verbose_name='опубликовано', default=False, **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ('name', )
