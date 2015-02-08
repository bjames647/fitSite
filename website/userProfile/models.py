from django.db import models
from django.contrib.auth.models import User


class fitUser(models.Model):
    user = models.OneToOneField(User)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    gender = models.EmailField()
