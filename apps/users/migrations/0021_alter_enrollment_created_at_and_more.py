# Generated by Django 4.1.1 on 2022-10-23 01:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_alter_rel_enrollment_lesson_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]