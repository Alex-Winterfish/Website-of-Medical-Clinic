# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand
from clinic.models import MedServiceModel

class Command(BaseCommand):
    '''Команда для добавления медицинских услуг.'''

    def handle(self, *args, **options):
        MedServiceModel.objects.all().delete()

        services = [
            {
                'name': 'Общий анализ крови',
                'description': 'Общий анализ крови'
            },
            {
                'name': 'Магнитно-резонансная томография',
                'description': 'Исследование организма на магнитно-оезонансном томографе'
            }
        ]

        for service_data in services:
            service, created = MedServiceModel.objects.get_or_create(**service_data)

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Добавлена услуга {service.name}.')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'{service.name} уже существует.')
                )