# -*- coding: UTF-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models
from users.validators import phone_number_validator


class CustomUser(AbstractUser):
    """Модель пользователя model: users.CustomUser"""

    last_name = models.CharField(
        max_length=200, verbose_name="Фамилия", help_text="введите фамилию", blank=True
    )
    first_name = models.CharField(
        max_length=100, verbose_name="Имя", help_text="введите имя", blank=True
    )
    patronymic = models.CharField(
        max_length=100,
        verbose_name="Отчество",
        help_text="введите отчество (при наличии)",
        blank=True,
    )
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(
        max_length=35,
        verbose_name="Phone",
        null=True,
        blank=True,
        help_text="Введите номер телефона",
    )
    country = models.CharField(
        max_length=50, verbose_name="Страна", help_text="Введите страну"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class FeedBackModel(models.Model):
    """Модель обратной связи пользователя"""

    theme = models.CharField(verbose_name="тема", max_length=100)
    feed_back = models.TextField(verbose_name="текст пользователя", max_length=2000)
    email = models.EmailField(verbose_name="электронная почта для обратной связи")

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = "Земачания пользвателя"
        verbose_name_plural = "Замечания пользователей"


class ContentModel(models.Model):
    """Модель контента сайта."""

    company = models.CharField(verbose_name="Медицинская компания", max_length=150)
    about = models.TextField(
        verbose_name="Описание медицинской компании", max_length=2000
    )
    email = models.EmailField(verbose_name="Электронная почта компании")
    phone = models.CharField(
        verbose_name="телефонный номер компании", validators=[phone_number_validator]
    )
    history = models.TextField(verbose_name="История компании", max_length=2000)
    values = models.TextField(verbose_name="Миссия и ценности", max_length=2000)
    address = models.CharField(verbose_name="Адрес клиники", max_length=200)
    map_address = models.URLField(
        verbose_name="Карта проезда(ссылка iframe)", max_length=2000
    )

    def __str__(self):
        return f"Контент для сайта компании {self.company}."

    class Meta:
        verbose_name = "компания"
        verbose_name_plural = "компании"
