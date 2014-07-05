from django.db import models
from django.contrib.auth.models import User

class fitUser(models.Model):
    user = models.OneToOneField(User)

    #email = models.OneToOneField(user, max_length=255)