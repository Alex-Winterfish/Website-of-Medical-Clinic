# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand
from clinic.models import MedStaffModel


class Command(BaseCommand):
    """Команда для добавления медицинских работников"""

    def handle(self, *args, **options):
        MedStaffModel.objects.all().delete()

        staff = [
            {
                "name": "Васютин Александр Анатольевич",
                "title": "Врач",
                "speciality": "рентгенолог",
                'photo': 'clinic/vasutin_md.jpg'
            },
            {
                "name": "Селезнев Александр Виторович",
                "title": "Врач",
                "speciality": "терапевт",
                'photo': 'clinic/seleznev_md.jpg'
            },
            {
                "name": "Бандурина Вера Александровна",
                "title": "Медсестра",
                'photo': 'clinic/vera_nurse.jpg'
            },
        ]

        for staff_data in staff:
            staff, created = MedStaffModel.objects.get_or_create(**staff_data)

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Добавлен {staff.title}: {staff.name}.")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"{staff.title} {staff.name} уже существует!")
                )
