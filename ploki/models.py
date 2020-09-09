from __future__ import unicode_literals
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    kuva = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    julkaistu_pvm = models.DateField()
    categories = models.ManyToManyField('Category', related_name='posts')
    kuvitusta = models.ImageField(blank=True)
    kuvitusta2 = models.ImageField(blank=True)
    kuvitusta3 = models.ImageField(blank=True)
    linkki = models.URLField(blank=True)
    linkkinimi = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_on',)


class Comment(models.Model):
    comment_author = models.CharField(max_length=60)
    comment_maili = models.CharField(max_length=60, blank=True)
    comment_body = models.TextField()
    comment_created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_author


class Play(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.name
