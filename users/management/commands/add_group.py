# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand
from users.models import CustomUser
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    """Команда для добавлнеия групп moders и staff_md."""

    help = "add groups moders and staff_md"

    def handle(self, *args, **kwargs):

        moder_group, created = Group.objects.get_or_create(
            name="moders"
        )  # создаем группу moders
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Добавлена группа {moder_group.name}.")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"Группа {moder_group.name} уже существует.")
            )
        # разрешения для группы moders
        change_appointmentmodel = Permission.objects.get(
            codename="change_appointmentmodel"
        )
        delete_appointmentmodel = Permission.objects.get(
            codename="delete_appointmentmodel"
        )
        view_appointmentmodel = Permission.objects.get(codename="view_appointmentmodel")
        add_medservicemodel = Permission.objects.get(codename="add_medservicemodel")
        change_medservicemodel = Permission.objects.get(
            codename="change_medservicemodel"
        )
        delete_medservicemodel = Permission.objects.get(
            codename="delete_medservicemodel"
        )
        view_medservicemodel = Permission.objects.get(codename="view_medservicemodel")
        add_medstaffmodel = Permission.objects.get(codename="add_medstaffmodel")
        change_medstaffmodel = Permission.objects.get(codename="change_medstaffmodel")
        delete_medstaffmodel = Permission.objects.get(codename="delete_medstaffmodel")
        view_medstaffmodel = Permission.objects.get(codename="view_medstaffmodel")
        change_contentmodel = Permission.objects.get(codename="change_contentmodel")
        delete_contentmodel = Permission.objects.get(codename="delete_contentmodel")
        view_contentmodel = Permission.objects.get(codename="view_contentmodel")
        add_contentmodel = Permission.objects.get(codename="add_contentmodel")
        change_customuser = Permission.objects.get(codename="change_customuser")
        delete_customuser = Permission.objects.get(codename="delete_customuser")
        view_customuser = Permission.objects.get(codename="view_customuser")
        delete_feedbackmodel = Permission.objects.get(codename="delete_feedbackmodel")
        view_feedbackmodel = Permission.objects.get(codename="view_feedbackmodel")

        moder_perm = [
            change_appointmentmodel,
            delete_appointmentmodel,
            view_appointmentmodel,
            add_medservicemodel,
            change_medservicemodel,
            delete_medservicemodel,
            view_medservicemodel,
            add_medstaffmodel,
            change_medstaffmodel,
            delete_medstaffmodel,
            view_medstaffmodel,
            change_customuser,
            delete_customuser,
            view_customuser,
            delete_feedbackmodel,
            view_feedbackmodel,
            add_contentmodel,
            change_contentmodel,
            delete_contentmodel,
            view_contentmodel,
        ]

        for perm in moder_perm:
            moder_group.permissions.add(perm)

        moder = {
            "last_name": "Каткин",
            "first_name": "Игорь",
            "patronymic": "Иванович",
            "username": "moder_1",
            "email": "moder_1@mail.com",
            "password": "pbkdf2_sha256$870000$cXDyxcfpSsVnOEgcjD0hd9$e8pQZzj6Q5G5P9MYSjAhJ7He5FEOxhktOcasUGtOxAQ=",
            "country": "Russia",
        }

        moder_user, created = CustomUser.objects.get_or_create(**moder)

        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Добавлен модератор {moder_user.username}")
            )
            moder_user.groups.add(moder_group)
        else:
            self.stdout.write(
                self.style.WARNING(f"Модератор уже существует {moder_user.username}")
            )
