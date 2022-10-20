from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from crypto.models import CryptoCurrency


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    crypto = models.ManyToManyField(CryptoCurrency)


    def __str__(self):
        return f'{self.user.username} Profile'



