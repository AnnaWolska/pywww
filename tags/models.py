from django.db import models
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return f"{self.name} with slug: {self.slug}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tagi"

    # @property
    # def tags_count(self):
    #     return self.name.count()
