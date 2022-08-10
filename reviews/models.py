from django.db import models


class Review(models.Model):
    user_name = models.CharField(max_length=255)
    review_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.user_name}: {self.review_text} ({self.rating})"
