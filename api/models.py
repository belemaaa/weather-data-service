from django.db import models


class Weather(models.Model):
    city = models.CharField(max_length=120, null=False, blank=False)
