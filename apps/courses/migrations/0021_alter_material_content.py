# Generated by Django 4.1.1 on 2022-10-25 22:10

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_alter_material_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='content',
            field=markdownx.models.MarkdownxField(blank=True, null=True),
        ),
    ]
