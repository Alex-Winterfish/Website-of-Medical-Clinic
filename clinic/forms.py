from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput

from clinic import models


class AppointmentForm(forms.ModelForm):
    """Форма для создания экземпляра model:clinic.models.AppointmentModel."""

    class Meta:
        model = models.AppointmentModel
        fields = ["ap_date", "ap_time"]

        widgets = {
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
