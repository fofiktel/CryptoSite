from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from crypto.models import CryptoCurrency


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_crypto = models.ManyToManyField(CryptoCurrency)

    def __str__(self):
        return f'{self.user.username} Profile'


class CryptoAssets(models.Model):
    crypto_currency_full_name = models.CharField(max_length=40, default='crypto')
    total_number_of_currency = models.FloatField(default=0)
    user_profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.crypto_currency_full_name} with total number {self.total_number_of_currency}'


class BuyInformation(models.Model):
    date_of_buying = models.DateField(default=timezone.now)
    amount_of_crypto = models.FloatField(default=0)
    purchase_price = models.FloatField(default=0)
    CryptoAssets = models.ForeignKey(CryptoAssets,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.purchase_price} {self.amount_of_crypto}'


class SoldInformation(models.Model):
    sold_date = models.DateField(default=timezone.now)
    amount_sold_crypto = models.FloatField(default=0)
    sold_price = models.FloatField(default=0)
    CryptoAssets = models.ForeignKey(CryptoAssets,on_delete=models.CASCADE,null=True)
