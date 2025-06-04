import re
from django.core.exceptions import ValidationError


def phone_number_validator(value):
    phone_regex = re.compile(
        r'^(\+?\d{1,3})?[\s\-]?$?\d{1,4}$?[\s\-]?\d{1,4}[\s\-]?\d{1,4}$'
    )
    if not phone_regex.match(value):
        raise ValidationError('Введите корректный телефонный номер.')