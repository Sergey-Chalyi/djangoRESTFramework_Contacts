# Generated by Django 5.1.2 on 2024-10-22 07:40

import contacts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=255, unique=True, validators=[contacts.models.validate_phone_number]),
        ),
    ]
