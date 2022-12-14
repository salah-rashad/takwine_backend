# Generated by Django 4.1.1 on 2022-11-01 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0029_alter_course_description_alter_course_imageurl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(db_column='category', null=True, on_delete=django.db.models.deletion.RESTRICT, to='courses.coursecategory'),
        ),
        migrations.AlterField(
            model_name='course',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
