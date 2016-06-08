from django.conf import settings
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Shop(models.Model):
    title = models.CharField(max_length=100)
    content_phone = models.CharField(max_length=100)
    content_adress = models.CharField(max_length=100)
    content_detail = models.TextField()
    photo = models.ImageField()

class Review(models.Model):
    post = models.ForeignKey(Shop)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)