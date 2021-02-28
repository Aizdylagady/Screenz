from datetime import date

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from pytils.translit import slugify

CHOICES = (
    ('actor', 'Актер'),
    ('director', 'Режисер'),
    ('producer', 'Продюсер'),
)


class Genre(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.CharField(primary_key=True, max_length=50)
    image = models.ImageField(upload_to='genres', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200, blank=True, null=True)
    video = models.FileField(upload_to='video')
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')
    description = models.TextField()
    image = models.ImageField(upload_to='movies', blank=True, null=True)
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveBigIntegerField(default=0, help_text="specify the amount in dollars")
    gross_in_usa = models.PositiveBigIntegerField(default=0, help_text="specify the amount in dollars")
    gross_in_the_world = models.PositiveBigIntegerField(default=0, help_text="specify the amount in dollars")
    country = models.CharField(max_length=100, default='USA')

    def __str__(self):
        return self.title


class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    role = models.CharField(max_length=20, choices=CHOICES)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='actors')
    image = models.ImageField(upload_to='authors', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Review(models.Model):
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=2000)
    parent = models.ForeignKey('self', related_name="children", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.user} - {self.movie}'