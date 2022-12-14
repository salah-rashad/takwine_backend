# Generated by Django 4.1.1 on 2022-10-12 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_alter_course_title'),
        ('users', '0013_alter_enrollment_currentlesson_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='currentLesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.lesson'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='currentMaterial',
            field=models.ForeignKey(blank=True, db_column='currentMaterialId', null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.material'),
        ),
    ]
