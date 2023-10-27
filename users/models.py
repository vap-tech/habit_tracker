from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """ User """
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    patronymic = models.CharField(max_length=35, verbose_name='отчество', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name} - {self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('first_name', 'last_name', 'patronymic')
