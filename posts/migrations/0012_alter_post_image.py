# Generated by Django 4.0 on 2022-03-01 12:23

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='posts/images/%Y/%m/%d/'),
        ),
    ]
