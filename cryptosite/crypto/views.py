from django.shortcuts import render,get_object_or_404
import requests
from .models import CryptoCurrency
from django.views import generic
from django.urls import reverse
from django.utils import timezone

def CryptoView (request):
    crypto_list = CryptoCurrency.objects.all()
    res = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order='
                       'market_cap_desc&per_page=100&page=1&sparkline=false')

    if (res.status_code == 200):
        count = 0
        for c in crypto_list:
            c.currency_id=res.json()[count]['id']
            c.CurrencyFullName = res.json()[count]['name']
            c.CurrencyAbbreviatedName =res.json()[count]['symbol']
            c.CostInUsd = res.json()[count]['current_price']
            c.MarketCap=res.json()[count]['market_cap']
            c.CirculatingSupply=res.json()[count]['circulating_supply']
            c.UpdateDate=timezone.now()
            c.ChangePrice=res.json()[count]['price_change_percentage_24h']
            c.save()
            count+=1

    context = {'crypto_list':crypto_list}
    return render(request,'crypto/CryptoList.html',context)


def DetailView(request,pk):
    crypto_currency = CryptoCurrency.objects.get(currency_id = pk)


    res = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids='
                      f'{crypto_currency.currency_id}&vs_currencies=usd&include_market_cap=true&include_24hr_change=true')

    crypto_currency.CostInUsd = res.json()[crypto_currency.currency_id]['usd']
    crypto_currency.MarketCap = res.json()[crypto_currency.currency_id]['usd_market_cap']
    crypto_currency.ChangePrice =res.json()[crypto_currency.currency_id]['usd_24h_change']

    context = {'crypto_currency': crypto_currency}
    return render(request, 'crypto/CryptoDetail.html', context)