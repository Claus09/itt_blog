# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField(null=True)
    mod_date = models.DateField(null=True)
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField(null=True)
    n_pingbacks = models.IntegerField(null=True)
    rating = models.IntegerField(null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.headline
