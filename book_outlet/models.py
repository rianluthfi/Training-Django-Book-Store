from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify # method to convert to type slug

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    # id field will automatically create by Django

    # add slug field
    slug = models.SlugField(default="", null=False, db_index=True) 
    # sample slug  --> Harry Potter 1 => harry-potter-1 
    # db_index can enhance to search
    # not all field can be indexed, because when saved data that have index, will decrease performance

    # using reverse to maintain url in index.html
    def get_absolute_url(self):
        # return reverse("book-detail", args=[self.id])
        return reverse("book-detail", args=[self.slug])
    
    # add validation when save
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    # add method to return show data
    def __str__(self):
        return f"{self.title} ({self.rating})"
