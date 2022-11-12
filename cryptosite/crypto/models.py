from django.utils import timezone
from django.db import models

# Create your models here.


class CryptoCurrency(models.Model):
    currency_id = models.CharField(max_length=40,default='crypto')
    CurrencyFullName = models.CharField(max_length=40)
    CurrencyAbbreviatedName = models.CharField(max_length=10)
    CostInUsd = models.FloatField(default=0)
    MarketCap = models.BigIntegerField(default=0)
    CirculatingSupply = models.BigIntegerField(default=0)
    UpdateDate = models.DateField(default=timezone.now)
    ChangePrice = models.FloatField(default=0)
    # # c = CryptoCurrency(CurrencyFullName=r['name']
    # ,CurrencyAbbreviatedName=r['symbol'],
    # CostInUsd=r['current_price'],
    # MarketCap= r['market_cap'],
    # MarketCap = r['market_cap'],UpdateDate=timezone.now(),ChangePrice = r['price_change_percentage_24h'])
    def __str__(self):
        return self.CurrencyFullName


# Create your models here.c =
