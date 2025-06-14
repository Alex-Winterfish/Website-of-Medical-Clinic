# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand
from clinic.models import MedServiceModel, MedStaffModel


class Command(BaseCommand):
    """Команда для добавления медицинских услуг."""

    def handle(self, *args, **options):
        MedServiceModel.objects.all().delete()

        services = [
            {
                "name": "Общий анализ крови",
                "description": "Общий анализ крови",
                "price": 1200,
                "photo": "clinic/blood_work.jpg",
                "med_spec": MedStaffModel.objects.get(title="Медсестра"),
            },
            {
                "name": "Магнитно-резонансная томография",
                "description": "Исследование организма на магнитно-оезонансном томографе",
                "price": 5550,
                "photo": "clinic/mri.jpg",
                "med_spec": MedStaffModel.objects.get(speciality="рентгенолог"),
            },
            {
                "name": "Осмотр у терапевта",
                "description": "Терапевтический осмотр у специалиста",
                "price": 2000,
                "photo": "clinic/checkup.jpg",
                "med_spec": MedStaffModel.objects.get(speciality="терапевт"),
            },
        ]

        for service_data in services:
            service, created = MedServiceModel.objects.get_or_create(**service_data)

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Добавлена услуга {service.name}.")
                )
            else:
                self.stdout.write(self.style.WARNING(f"{service.name} уже существует."))
