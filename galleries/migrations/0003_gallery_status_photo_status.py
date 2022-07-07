# Generated by Django 4.0 on 2022-03-25 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0002_gallery_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='status',
            field=models.CharField(choices=[('1', 'new'), ('2', 'hide'), ('3', 'published')], default='1', max_length=10),
        ),
        migrations.AddField(
            model_name='photo',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[('1', 'new'), ('2', 'hide'), ('3', 'published')], default='1'),
        ),
    ]