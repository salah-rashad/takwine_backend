# Generated by Django 4.1.1 on 2022-11-15 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0036_remove_question_exam_question_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(blank=True, db_column='category', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.coursecategory'),
        ),
        migrations.AlterField(
            model_name='coursecategory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
