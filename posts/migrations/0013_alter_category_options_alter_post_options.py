# Generated by Django 4.0 on 2022-04-26 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_alter_post_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategoria', 'verbose_name_plural': 'Kategorie'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posty'},
        ),
    ]