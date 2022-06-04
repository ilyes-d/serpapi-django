from django.db import models
from django.forms import CharField

# Create your models here.

class Author(models.Model):
    gs_account = models.URLField(blank=True, null=True)
    author_citations = models.IntegerField(blank=True)

class Post(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name