# Generated by Django 4.1.1 on 2022-10-06 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolledcourse',
            name='progress',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthDate',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
