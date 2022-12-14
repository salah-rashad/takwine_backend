# Generated by Django 4.1.1 on 2022-11-01 02:34

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0028_alter_question_exam_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='imageUrl',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='pdfUrl',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='videoUrl',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='coursecategory',
            name='color',
            field=colorfield.fields.ColorField(blank=True, default='#C1C1C1', image_field=None, max_length=18, null=True, samples=None),
        ),
        migrations.AlterField(
            model_name='coursecategory',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='coursecategory',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='questionchoice',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
