from django.db import models
from django.utils.translation import gettext as _


class Movies(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    published = models.BooleanField(default=False)
    yearOfPublished = models.IntegerField(default=False)
    duration = models.IntegerField()

    def __str__(self):
        return self.title
