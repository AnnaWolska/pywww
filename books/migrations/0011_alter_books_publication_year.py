# Generated by Django 4.0 on 2022-04-19 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_books_decription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='publication_year',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
