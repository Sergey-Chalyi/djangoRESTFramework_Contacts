from django.db import models
from django.core.exceptions import ValidationError
import re

def validate_phone_number(value):
    # Регулярное выражение для проверки, что номер начинается с + и далее идут цифры
    if not re.match(r'^\+\d+$', value):
        raise ValidationError('Phone number must start with + and contain only numbers.')

class Contact(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=255, unique=True, null=False, blank=False, validators=[validate_phone_number])
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)

    def __str__(self):
        return f'{self.first_name}_{self.last_name}'
