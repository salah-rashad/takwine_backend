# Generated by Django 4.1.1 on 2022-10-06 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_options_alter_course_lessons_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='course',
        ),
        migrations.CreateModel(
            name='CourseLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering', models.PositiveIntegerField(db_index=True, default=0)),
                ('course', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('lesson', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='courses.lesson')),
            ],
            options={
                'ordering': ['ordering'],
            },
        ),
        migrations.RemoveField(
            model_name='course',
            name='lessons',
        ),
        migrations.AddField(
            model_name='course',
            name='lessons',
            field=models.ManyToManyField(
                blank=True, related_name='courses', through='courses.CourseLesson', to='courses.lesson'),
        ),
    ]