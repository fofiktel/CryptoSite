
from django.db import models
# Create your models here.


class CryptoCurrency(models.Model):
    CurrencyFullName = models.CharField(max_length=40)
    CurrencyAbbreviatedName = models.CharField(max_length=10)
    CostInUsd = models.FloatField(default=0)
    MarketCap = models.IntegerField(default=0)
    CirculatingSupply = models.IntegerField(default=0)

    def __str__(self):
        return self.CurrencyFullName

# Create your models here.
