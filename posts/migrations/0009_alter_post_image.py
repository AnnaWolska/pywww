# Generated by Django 4.0 on 2022-01-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='posts/images/%Y/%m/%d/'),
        ),
    ]
