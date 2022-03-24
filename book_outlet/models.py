from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(null=True, max_length=100)
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f"{self.title} ({self.rating})"

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.id])  # type: ignore

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
