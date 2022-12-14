# Generated by Django 4.1.1 on 2022-12-12 22:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0007_remove_documentcategory_color_documentfile_name_and_more'),
        ('users', '0035_alter_certificate_unique_together_coursebookmark'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentBookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='documents.document')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Document Bookmark',
                'verbose_name_plural': 'Document Bookmarks',
                'unique_together': {('user', 'document')},
            },
        ),
    ]
