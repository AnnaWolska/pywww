# Generated by Django 4.0 on 2022-01-20 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_exemple_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='posts/images/%Y/%m/%d?'),
        ),
    ]