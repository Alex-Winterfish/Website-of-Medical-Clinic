from django.test import TestCase, Client
from clinic import models
from users.models import CustomUser
from django.utils.timezone import datetime


class AppointmentTestCase(TestCase):

    def setUp(self):
        staff = [
            {
                "name": "Васютин Александр Анатольевич",
                "title": "Врач",
                "speciality": "рентгенолог",
                "photo": "clinic/staff/radiologist_mv2.jpg",
            },
            {
                "name": "Селезнев Александр Виторович",
                "title": "Врач",
                "speciality": "терапевт",
                "photo": "clinic/staff/therapist_mv2.jpg",
            },
            {
                "name": "Бандурина Вера Александровна",
                "title": "Медсестра",
                "photo": "clinic/staff/nurse.jpg",
            },
        ]

        for staff_data in staff:
            models.MedStaffModel.objects.create(**staff_data)

        services = [
            {
                "name": "Общий анализ крови",
                "description": "Общий анализ крови",
                "price": 1200,
                "photo": "clinic/blood_work.jpg",
                "med_spec": models.MedStaffModel.objects.get(title="Медсестра"),
            },
            {
                "name": "Магнитно-резонансная томография",
                "description": "Исследование организма на магнитно-оезонансном томографе",
                "price": 5550,
                "photo": "clinic/mri.jpg",
                "med_spec": models.MedStaffModel.objects.get(speciality="рентгенолог"),
            },
            {
                "name": "Осмотр у терапевта",
                "description": "Терапевтический осмотр у специалиста",
                "price": 2000,
                "photo": "clinic/checkup.jpg",
                "med_spec": models.MedStaffModel.objects.get(speciality="терапевт"),
            },
        ]

        for service_data in services:
            models.MedServiceModel.objects.create(**service_data)

        user = {
            "last_name": "Иванов",
            "first_name": "Иван",
            "patronymic": "Иванович",
            "username": "user_1",
            "email": "user_1@mail.com",
            "password": "pbkdf2_sha256$870000$cXDyxcfpSsVnOEgcjD0hd9$e8pQZzj6Q5G5P9MYSjAhJ7He5FEOxhktOcasUGtOxAQ=",
            "country": "Russia",
        }

        CustomUser.objects.create(**user)

    def test_appointment_create(self):
        """Тест проверяет создание model:clinic.models.AppointModel."""

        appointment = {
            "ap_date": datetime.now(),
            "ap_time": datetime.now(),
            "med_serv": models.MedServiceModel.objects.get(name="Общий анализ крови"),
            "patient": CustomUser.objects.get(email="user_1@mail.com"),
        }

        app_bw = models.AppointmentModel.objects.create(**appointment)

        self.assertEqual(
            app_bw.patient, CustomUser.objects.get(email="user_1@mail.com")
        )

    def test_appointment_create_view(self):
        """Тест проверяет создание model:clinic.models.AppointmentModel."""

        appointment = {
            "ap_date": datetime.now(),
            "ap_time": datetime.now(),
        }
        client = Client()

        response = client.post(
            f"/appointment/create/{models.MedServiceModel.objects.get(name='Общий анализ крови').id}/",
            **appointment,
        )
        self.assertEqual(response.status_code, 200)
