# Generated by Django 4.1.1 on 2022-10-25 21:39

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_alter_rel_lesson_material_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='content',
            field=markdownx.models.MarkdownxField(blank=True, null=True),
        ),
    ]