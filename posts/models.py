from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now, timedelta

class CheckAgeMixin:

    def is_older_than_n_days(self, n=1):
        delta = timedelta(days=n)
        return now() - self.created > delta

class Timestamped(models.Model, CheckAgeMixin):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(Timestamped):
    title = models.CharField(verbose_name="Tytuł", max_length=255)
    content = models.TextField(verbose_name="Treść")
    published = models.BooleanField(verbose_name="Opublikowany",default=False)
    sponsored = models.BooleanField(verbose_name="Sponsorowany",default=False)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, default="1", related_name="posts")
    tags = models.ManyToManyField('tags.Tag',related_name="posts")
    categories = models.ManyToManyField('Category', related_name="posts")
    exemple_file = models.FileField(upload_to='posts/examples', blank=True, null=True)
    image = models.ImageField(upload_to="posts/images/%Y/%m/%d/", blank=True, null=True)

    def __str__(self):
        return f"{self.id} {self.title} {self.content} {self.created} {self.modified} {self.published} {self.sponsored} {self.user} {self.tags} {self.categories} {self.exemple_file} {self.image}"

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} {self.description}"