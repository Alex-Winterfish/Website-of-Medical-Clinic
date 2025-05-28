# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand
from users.models import CustomUser

class Command(BaseCommand):
    '''Команда для длобавления пользователей'''
    def handle(self, *args, **kwargs):
        CustomUser.objects.all().delete()

        users = [
            {
                'last_name': 'Иванов',
                'first_name': 'Иван',
                'patronymic': 'Иванович',
                'username': 'user_1',
                "email": "user_1@mail.com",
                "password": "pbkdf2_sha256$870000$cXDyxcfpSsVnOEgcjD0hd9$e8pQZzj6Q5G5P9MYSjAhJ7He5FEOxhktOcasUGtOxAQ=",
                "country": "Russia",
            },
            {
                'last_name': 'Петров',
                'first_name': 'Петр',
                'patronymic': 'Петрович',
                'username': 'user_2',
                "email": "user_2@mail.com",
                "password": "pbkdf2_sha256$870000$k9lZWga6YEePGlyyoZZp0u$dACFQOuJB1EzKRCTvNwnMkr105fVqJ2vUYzsSv9WldQ=",
                "country": "Russia",
            },
        ]

        for user_data in users:
            user, created = CustomUser.objects.get_or_create(**user_data)

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Добавлен пользователь {user.username}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Пользователь уже существует {user.username}")
                )
