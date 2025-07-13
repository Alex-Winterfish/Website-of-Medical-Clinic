from django.test import TestCase, Client
from clinic import models
from users.models import CustomUser
from django.shortcuts import reverse


class ResultsTestCase(TestCase):
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

        appointments = [
            {
                "ap_date": "2025-03-14",
                "ap_time": "10:00:00",
                "med_serv": models.MedServiceModel.objects.get(
                    name="Общий анализ крови"
                ),
                "patient": CustomUser.objects.get(email="user_1@mail.com"),
            },
            {
                "ap_date": "2025-03-16",
                "ap_time": "12:00:00",
                "med_serv": models.MedServiceModel.objects.get(
                    name="Осмотр у терапевта"
                ),
                "patient": CustomUser.objects.get(email="user_1@mail.com"),
            },
        ]

        for app in appointments:
            models.AppointmentModel.objects.create(**app)

    def test_result_create(self):
        """Тестирование создание экземпляра model:clinic.ResultModel."""

        result = {
            "result_date": "2025-03-18",
            "appointment": models.AppointmentModel.objects.get(ap_date="2025-03-14"),
            "result": "Результат анализа крови.",
            "patient": CustomUser.objects.get(email="user_1@mail.com"),
        }

        models.ResultModel.objects.create(**result)

        self.assertTrue(
            models.ResultModel.objects.filter(result_date="2025-03-18").exists()
        )

    def test_results_view(self):
        """Тест для проверки создания model:clinic.models.ResultsModel из шаблона clinic/moder_page.html."""

        url = reverse(
            "results:create_result",
            kwargs={"pk": models.AppointmentModel.objects.get(ap_date="2025-03-14").id},
        )

        client = Client()

        login_success = client.login(email="user_1@mail.com", password="12345")
        self.assertTrue(login_success)

        result = {
            "appointment": models.AppointmentModel.objects.get(ap_date="2025-03-14").id,
            "result": "Результат анализа крови.",
        }

        response = client.post(url, result)
        self.assertTrue(
            models.ResultModel.objects.filter(
                result="Результат анализа крови."
            ).exists()
        )
        self.assertEqual(response.status_code, 302)

    def test_result_list_view(self):
        """Тест для проверки получния списка model:models.clinic.ResultModel."""

        results = [
            {
                "result_date": "2025-03-18",
                "appointment": models.AppointmentModel.objects.get(
                    ap_date="2025-03-16"
                ),
                "result": "Результат осмотра у терапевта.",
                "patient": CustomUser.objects.get(email="user_1@mail.com"),
            },
            {
                "result_date": "2025-03-18",
                "appointment": models.AppointmentModel.objects.get(
                    ap_date="2025-03-14"
                ),
                "result": "Результат анализа крови.",
                "patient": CustomUser.objects.get(email="user_1@mail.com"),
            },
        ]

        for res in results:
            models.ResultModel.objects.create(**res)

        self.assertEqual(models.ResultModel.objects.count(), 2)
