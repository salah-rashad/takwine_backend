# Generated by Django 4.1.1 on 2022-12-14 20:42

from django.db import migrations, models
import takwine.models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0010_documentcategory_color_documentcategory_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='imageUrl',
            field=models.ImageField(blank=True, default=None, max_length=255, null=True, upload_to='uploads/images/'),
        ),
        migrations.AlterField(
            model_name='documentfile',
            name='file',
            field=models.FileField(help_text='* Maximum upload file size 5 MB.', upload_to='uploads/files/', validators=[takwine.models.TakwineFile.file_size_validator]),
        ),
    ]