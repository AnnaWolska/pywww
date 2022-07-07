# Generated by Django 4.0 on 2022-04-26 12:47

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0007_alter_photo_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Galeria', 'verbose_name_plural': 'Galerie'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Zdjęcie', 'verbose_name_plural': 'Zdjęcia'},
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]