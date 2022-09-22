from django.contrib.auth.models import User
from django.db import models
from .utils import *


class Images(models.Model):
    image = models.ImageField(upload_to='product/%d')

    def __str__(self):
        return self.image.url

    def save(self ,*args ,**kwargs):
            super().save()
            img = Image.open(self.image.path)
            img_new = crop_center(img ,min(img.size))
            img_new.save(self.image.path)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    data = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    images = models.ManyToManyField(Images, symmetrical=False)

    def __str__(self):
        return self.name


