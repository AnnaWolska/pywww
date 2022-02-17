from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    title = models.CharField(max_length=255)
    decription = models.TextField()
    available = models.BooleanField(default=False)
    publication_year = models.SmallIntegerField()
    author = models.CharField(max_length=64)
    tags = models.ManyToManyField('tags.Tag', related_name="books")
    image = models.ImageField(upload_to="books/covers/%Y/%m/%d/", blank=True, null=True)

    def __str__(self):
        return f"{self.id} {self.title} {self.decription} {self.available} {self.publication_year} {self.author} {self.tags} {self.image}"
