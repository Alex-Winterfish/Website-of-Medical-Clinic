from django.test import TestCase, Client
from clinic import models
from users.models import CustomUser
from django.shortcuts import reverse


class ServicesTestCase(TestCase):

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

    def test_service_create(self):
        """Тестирование создания model:clinic.models.MedServiceModel."""

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

        self.assertEqual(models.MedServiceModel.objects.count(), 3)

    def test_services_list_view(self):
        """Тестирование получения экземпляров model:clinic.models.MedServiceModel
        в шаблоне clinic/services.html."""

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

        url = reverse("services:med_services")

        client = Client()

        response = client.get(url)
        self.assertEqual(response.context.get("object_list").count(), 3)
        self.assertEqual(response.status_code, 200)
