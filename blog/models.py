from django.db import models
from django.utils import timezone
from PIL import Image


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True)


class Category(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()


def publish(self):
    self.published_date = timezone.now()
    self.save()


def __str__(self):
    return self.title


def __str__(self):
    return self.name
