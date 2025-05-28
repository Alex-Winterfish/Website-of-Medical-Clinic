# -*- coding: UTF-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Модель пользователя model: users.CustomUser"""
    last_name = models.CharField(max_length=200, verbose_name='Фамилия', help_text='введите фамилию', blank=True)
    first_name = models.CharField(max_length=100, verbose_name='Имя', help_text='введите имя', blank=True)
    patronymic = models.CharField(max_length=100, verbose_name='Отчество', help_text='введите отчество (при наличии)', blank=True)
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
