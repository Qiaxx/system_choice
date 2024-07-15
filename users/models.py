from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    date_born = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    address = models.CharField(
        max_length=255, verbose_name="Место регистрации", blank=True, null=True
    )
    citizenship_rf = models.BooleanField(
        default=False, verbose_name="Гражданство РФ", blank=True, null=True
    )
    status_choice = models.BooleanField(
        default=False, verbose_name="Статус голосования", blank=True, null=True
    )
    token = models.CharField(
        max_length=100, verbose_name="Токен", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
