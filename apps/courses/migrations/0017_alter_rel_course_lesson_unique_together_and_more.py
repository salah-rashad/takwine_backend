# Generated by Django 4.1.1 on 2022-10-18 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_alter_course_title'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rel_course_lesson',
            unique_together={('course', 'lesson')},
        ),
        migrations.AlterUniqueTogether(
            name='rel_lesson_material',
            unique_together={('lesson', 'material')},
        ),
        migrations.AlterUniqueTogether(
            name='rel_material_attachment',
            unique_together={('material', 'attachment')},
        ),
        migrations.AlterUniqueTogether(
            name='rel_material_component',
            unique_together={('material', 'component')},
        ),
    ]