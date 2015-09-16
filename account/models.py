from django.db import models

from django.contrib.auth.models import User, UserManager


class Account(User):
    timezone = models.FloatField(default=0)
    objects = UserManager()
