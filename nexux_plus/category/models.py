from django.db import models
from django import forms
class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    is_main = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField()
    def __str__(self):
        return self.name

class Region (models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    sorting = models.SmallIntegerField(null=False, blank=False)

    def __str__(self):
        return self.name

class Brand (models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name


