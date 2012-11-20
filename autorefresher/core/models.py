from django.db import models


class LastChange(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    refreshed = models.BooleanField()

