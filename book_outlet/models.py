from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    # id field will automatically create by Django

    # using reverse to maintain url in index.html
    def get_absolute_url(self):
        return reverse("book-detail", args=[self.id])
    
    # add method to return show data
    def __str__(self):
        return f"{self.title} ({self.rating})"
