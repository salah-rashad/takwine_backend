# Generated by Django 4.1.1 on 2022-12-12 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0041_materialfile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['ordering'], 'verbose_name': 'Question', 'verbose_name_plural': 'Exam Questions'},
        ),
    ]