# Generated by Django 4.1 on 2022-08-10 13:59

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(validators=[django.core.validators.MaxValueValidator(limit_value=datetime.date(2022, 8, 10))]),
        ),
    ]
