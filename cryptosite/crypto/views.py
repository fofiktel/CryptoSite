from django.shortcuts import render,get_object_or_404
import requests
from .models import CryptoCurrency
from django.views import generic
from django.urls import reverse
from django.utils import timezone

def CryptoView (request):


    res = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin%2Cethereum%2Ctether%2Cusd-coin%2Cbinancecoin%2Cripple%2Cbinance-usd%2Ccardano%2Csolana%2Cdogecoin%2Cpolkadot%2Cmatic-network%2Cshiba-inu%2Cdai%2Ctron%2Cstaked-ether%2Cuniswap%2Cwrapped-bitcoin%2Cavalanche-2%2Cokb%2Cleo-token%2Clitecoin%2Ccosmos%2Cchainlink%2Cethereum-classic%2Cftx-token%2Cstellar%2Cquant-network%2Ccrypto-com-chain%2Cmonero%2Cnear%2Calgorand%2Cbitcoin-cash%2Cterra-luna%2Cvechain%2Cflow%2Cfilecoin%2Chedera-hashgraph%2Capecoin%2Cfrax%2Celrond-erd-2%2Cchain-2%2Cinternet-computer%2Ctezos%2Caave%2Cthe-sandbox%2Cdecentraland%2Caxie-infinity%2Ceos%2Ctokenize-xchange%2Cmaker%2Clido-dao%2Chuobi-token%2Ctheta-token%2Captos%2Ccompound-usd-coin%2Cchiliz%2Ckucoin-shares%2Cbitcoin-cash-sv%2Cpaxos-standard%2Ctrue-usd%2Cusdd%2Cbittorrent%2Cecash%2Ciota%2Cethereum-pow-iou%2Czcash%2Cgatechain-token%2Ccdai%2Cpancakeswap-token%2Cthe-graph%2Chelium%2Chavven%2Cosmosis%2Cneo%2Ccompound-ether%2Cradix%2Cfantom%2Cevmos%2Carweave%2Cpax-gold%2Ccurve-dao-token%2Cnexo%2Cethereum-name-service%2Cbitdao%2Ccasper-network%2Ctrust-wallet-token%2Czilliqa%2Cfrax-share%2Cdash%2Cthorchain%2Cklay-token%2Cenjincoin%2Cxdce-crowd-sale%2Cbasic-attention-token%2Crocket-pool%2Ctether-gold%2Ckava%2Cblockstack%2Ccelsius-degree-token&order=market_cap_desc&per_page=100&page=1&sparkline=false')
    count = 0
    if (res.status_code==200):
        for r in res.json():
            c = CryptoCurrency.objects.get(currency_id =r['id'])
            c.CostInUsd = r['current_price']
            c.MarketCap = r['market_cap']
            c.CirculatingSupply = r['circulating_supply']
            c.UpdateDate = timezone.now()
            c.ChangePrice = r['price_change_percentage_24h']
            c.save(force_update=True)
            print("success",count)
            count+=1
    crypto_list = CryptoCurrency.objects.order_by('-MarketCap')
    context = {'crypto_list':crypto_list}
    return render(request,'crypto/CryptoList.html',context)


def DetailView(request,pk):
    crypto_currency = get_object_or_404(CryptoCurrency,currency_id = pk)


    res = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids='
                      f'{crypto_currency.currency_id}&vs_currencies=usd&include_market_cap=true&include_24hr_change=true')

    crypto_currency.CostInUsd = res.json()[crypto_currency.currency_id]['usd']
    crypto_currency.MarketCap = res.json()[crypto_currency.currency_id]['usd_market_cap']
    crypto_currency.ChangePrice =res.json()[crypto_currency.currency_id]['usd_24h_change']

    context = {'crypto_currency': crypto_currency}
    return render(request, 'crypto/CryptoDetail.html', context)



# for c,r in zip(crypto_list,res.json()):
        #     print(r['id'],c.currency_id)
        #     c.currency_id = r['id']
        #     c.CurrencyFullName = r['name']
        #     c.CurrencyAbbreviatedName =r['symbol']
        #     c.CostInUsd = r['current_price']
        #     c.MarketCap=r['market_cap']
        #     c.CirculatingSupply=r['circulating_supply']
        #     c.UpdateDate=timezone.now()
        #     c.ChangePrice=r['price_change_percentage_24h']
        #     c.save(force_update=True)