# Generated by Django 4.1.1 on 2022-11-13 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_alter_certificate_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='currentLesson',
        ),
        migrations.RemoveField(
            model_name='enrollment',
            name='currentMaterial',
        ),
    ]
