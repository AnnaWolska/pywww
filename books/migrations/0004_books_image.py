# Generated by Django 4.0 on 2022-02-14 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_books_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='image',
            field=models.ImageField(null=True, upload_to='media/books/covers/%Y/%m/%d/'),
        ),
    ]
