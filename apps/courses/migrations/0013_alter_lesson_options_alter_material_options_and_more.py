# Generated by Django 4.1.1 on 2022-10-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_alter_course_description_alter_course_imageurl_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['ordering'], 'verbose_name': 'Lesson', 'verbose_name_plural': 'Courses Lessons'},
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'ordering': ['ordering'], 'verbose_name': 'Material', 'verbose_name_plural': 'Courses Materials'},
        ),
        migrations.AlterModelOptions(
            name='materialattachment',
            options={'ordering': ['ordering'], 'verbose_name': 'Attachment', 'verbose_name_plural': 'Material Attachments'},
        ),
        migrations.AlterModelOptions(
            name='materialcomponent',
            options={'ordering': ['ordering'], 'verbose_name': 'Component', 'verbose_name_plural': 'Material Components'},
        ),
        migrations.RenameField(
            model_name='course',
            old_name='status',
            new_name='enabled',
        ),
        migrations.AlterField(
            model_name='materialcomponent',
            name='data',
            field=models.TextField(blank=True, max_length=550),
        ),
    ]