from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Bullscows(models.Model):
    """ Cteating game instance for current user, containing
        answer and list of user's tries"""

    answer = models.CharField(max_length=4, blank=True)
    try_string = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game')
