from django.db import models


class Writer(models.Model):
    name = models.CharField(max_length=200)


class Book(models.Model):
    author = models.ForeignKey(Writer, related_name='books', on_delete=models.CASCADE)
    name = models.JSONField()