from django import forms
from django.forms import DateInput, Select, Textarea
from clinic import models


class AppointmentForm(forms.ModelForm):
    """Форма для создания экземпляра model:clinic.models.AppointmentModel."""

    class Meta:
        model = models.AppointmentModel
        fields = ["med_serv", "ap_date", "ap_time"]

        widgets = {
            "med_serv": Select(
                attrs={"class": "form-control", "placeholder": "Выберите услуг"}
            ),
            "ap_date": DateInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Выберите дату",
                    "type": "date",  # чтобы активировать встроенный календарь браузера
                }
            ),
            "ap_time": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Выберите время",
                    "type": "time",  # для времени
                }
            ),
        }


class ResultForm(forms.ModelForm):
    """Форма для создания экземпляра model:clinic.models.ResultModel."""

    class Meta:
        model = models.ResultModel
        fields = ["appointment", "result"]

        widgets = {
            "appointment": Select(
                attrs={"class": "form-control", "placeholder": "Выберите назначение"}
            ),
            "result": Textarea(
                attrs={"class": "form-control", "placeholder": "Напишите заключение"}
            ),
        }


"""
class ServiceForm(forms.ModelForm):
    '''Форма для создания model:clinic.models.MedServiceModel.'''
    class Meta:
        model = models.MedServiceModel
        fields = ['name', 'description', 'price', 'photo', 'med_spec']
        widgets = {
            'name': {"class": "form-control", "placeholder": "Назмание медицинской услуги"},
            'description': Textarea(attrs={"class": "form-control", "placeholder": "Напишите заключение"}),
            'price': '',
            'photo': '',
            'med_spec': Select(
                attrs={"class": "form-control", "placeholder": "Выберите назначение"}
            ),
        }"""
