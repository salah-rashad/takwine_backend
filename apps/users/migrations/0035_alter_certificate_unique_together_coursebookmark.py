# Generated by Django 4.1.1 on 2022-11-14 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0036_remove_question_exam_question_lesson'),
        ('users', '0034_alter_certificate_result_alter_completelesson_result'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='certificate',
            unique_together={('user', 'course')},
        ),
        migrations.CreateModel(
            name='CourseBookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Course Bookmark',
                'verbose_name_plural': 'Course Bookmarks',
                'unique_together': {('user', 'course')},
            },
        ),
    ]