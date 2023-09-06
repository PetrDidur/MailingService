from django.contrib.auth.models import AbstractUser
from django.db import models
from constants import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='user/', **NULLABLE, verbose_name='аватарка')
    phone = models.IntegerField(**NULLABLE, verbose_name='телефон')
    country = models.CharField(**NULLABLE, max_length=100, verbose_name='страна')
    is_active = models.BooleanField(default=False, verbose_name='активность')
    verification_key = models.IntegerField(**NULLABLE, verbose_name='ключ')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

        permissions = [
            ('can_change_user_is_active', 'Can change user is active'),
        ]


