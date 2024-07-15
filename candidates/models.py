from django.db import models
from django.core.exceptions import ValidationError
from datetime import date


class Candidate(models.Model):
    # Основные данные
    full_name = models.CharField(
        max_length=255, verbose_name="Ф.И.О.", blank=False, null=False
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения", blank=True, null=True
    )
    place_of_birth = models.CharField(
        max_length=255, verbose_name="Место рождения", blank=True, null=True
    )
    photo = models.ImageField(
        upload_to="candidates/photos/", verbose_name="Фотография", blank=True, null=True
    )

    # Контактная информация
    official_website = models.URLField(
        verbose_name="Официальный сайт", blank=True, null=True
    )
    social_media_links = models.TextField(
        verbose_name="Социальные сети", blank=True, null=True
    )
    age = models.PositiveIntegerField(
        verbose_name="Возраст", blank=True, null=True
    )

    # Образование
    universities = models.TextField(verbose_name="Университеты", blank=True, null=True)
    degrees = models.TextField(verbose_name="Степени", blank=True, null=True)

    # Профессиональный опыт
    work_experience = models.TextField(
        verbose_name="Рабочие места", blank=True, null=True
    )
    political_experience = models.TextField(
        verbose_name="Опыт в политике", blank=True, null=True
    )

    # Политическая платформа
    goals_and_objectives = models.TextField(
        verbose_name="Цели и задачи", blank=True, null=True
    )
    projects_and_initiatives = models.TextField(
        verbose_name="Проекты и инициативы", blank=True, null=True
    )

    # История и достижения
    awards_and_recognitions = models.TextField(
        verbose_name="Награды и признания", blank=True, null=True
    )
    key_achievements = models.TextField(
        verbose_name="Основные достижения", blank=True, null=True
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Кандидат"
        verbose_name_plural = "Кандидаты"
