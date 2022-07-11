from django.db import models
from Videos.models import Video
from django.contrib.auth.models import User
from django.utils import timezone

class Chanel(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"""
User: {self.user.username},
creation date: {self.user.date_joined}
"""