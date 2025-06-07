from django.test import TestCase, Client
from clinic import models
from users.models import ContentModel
from django.shortcuts import reverse


class ServicesTestCase(TestCase):

    def test_create_staff(self):
        """Тестирование создание модели model:clinic.models.MedStaffModel."""
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

        self.assertEqual(models.MedStaffModel.objects.count(), 3)

    def test_staff_list_view(self):
        """Тестирование получение списка model:clinic.models.MedStaffModel
        в шаблоне clinic/company_page.html"""
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

        company = {
            "company": "MedService",
            "about": "О нас",
            "email": "example@mail.com",
            "phone": "8(800)888-88-88",
            "history": "Наша история",
            "values": "Наши ценности",
            "address": "ул. Ленина",
            "map_address": "http://map.com/",
        }

        ContentModel.objects.create(**company)

        url = reverse("staff:med_personal")

        client = Client()

        response = client.get(url)
        self.assertEqual(response.context.get("object_list").count(), 3)
        self.assertEqual(response.status_code, 200)
