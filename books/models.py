from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


class Author(models.Model):
    name = models.CharField(max_length=255)
    birth_year = models.IntegerField(null=True, blank=True)
    death_year = models.IntegerField(null=True, blank=True)
    biogram = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.birth_year} -)"


class Books(models.Model):
    title = models.CharField(max_length=255)
    decription = models.TextField(null=True, blank=True)
    available = models.BooleanField(default=False)
    publication_year = models.SmallIntegerField(null=True, blank=True)
    # author = models.ManyToManyField(Author, related_name="volumes")
    # author = models.CharField(max_length=64)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="publications",null=True, blank=True)
    tags = models.ManyToManyField('tags.Tag', related_name="books")
    image = ImageField(upload_to="books/covers/%Y/%m/%d/", blank=True, null=True)

    def __str__(self):
        return f"{self.id} {self.title} {self.decription} {self.available} {self.publication_year} {self.author} {self.tags} {self.image}"


class Borrow(models.Model):
    book = models.ForeignKey("Books", on_delete=models.CASCADE, related_name="borrows")
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="borrows")
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.book} {self.user} {self.borrow_date} {self.return_date}"


