from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=32)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=128)
    excerpt = models.CharField(max_length=255)
    # TODO: change image_name
    image_name = models.CharField(max_length=128)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(allow_unicode=True, unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, related_name="posts", null=True
    )
    tags = models.ManyToManyField(Tag)  # null=True?
