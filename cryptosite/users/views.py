from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .forms import UserRegisterForm


from .models import Profile, CryptoAssets
from crypto.models import CryptoCurrency


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('accounts:profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#Пофискить хуюню с ценой
@login_required
def profile(request):

    user_profile = get_object_or_404(Profile, user=request.user)
    assets = user_profile.cryptoassets_set.all()
    crypto_dict = {}
    for a in assets:

        current_price = CryptoCurrency.objects.get(CurrencyFullName=a.crypto_currency_full_name).CostInUsd*a.total_number_of_currency
        buy_inf = a.buyinformation_set.all()
        buy_price =0
        income = 0
        for inf in buy_inf:
            buy_price += inf.purchase_price*inf.amount_of_crypto

        income = (current_price / buy_price) * 100 - 100
        crypto_dict[a.crypto_currency_full_name] = {'current_price': current_price,'buy_price':buy_price,'income': income}


    print(crypto_dict)

    context = {
        'user_profile': user_profile,
        'crypto_dict': crypto_dict,
    }
    return render(request, 'users/profile.html', context)


def add_favorite_cryptocurrency(request):
    try:
        user_profile = get_object_or_404(Profile, user=request.user)
    except Profile.DoesNotExist:
        return HttpResponseNotFound("<h2>Profile not found</h2>")

    if request.method == "POST":
        try:
            user_profile.favorite_crypto.add(CryptoCurrency.objects.
                                             get(CurrencyFullName=request.POST.get("cryptocurrency_name")))
            user_profile.save()
        except CryptoCurrency.DoesNotExist:
            return HttpResponseNotFound("<h2>CryptoCurrency not found</h2> "
                                        "<a href="'http://127.0.0.1:8000/accounts/profile/'">Return to profile</a>")
    return HttpResponseRedirect("http://127.0.0.1:8000/accounts/profile/")


def delete_favorite_cryptocurrency(request, pk):
    user_profile = get_object_or_404(Profile, user=request.user)
    user_profile.favorite_crypto.remove(CryptoCurrency.objects.get(currency_id=pk))
    return HttpResponseRedirect("http://127.0.0.1:8000/accounts/profile/")


def additional_information_about_assets(request, pk):

    crypto_asset = Profile.objects.get(user=request.user).cryptoassets_set.get(id=pk)
    context = {
        'crypto_asset': crypto_asset
    }
    return render(request, 'users/buy_information.html', context)


def add_new_crypto_assets_page(request):
    return render(request,'users/buy_form.html')


def add_crypto_assets(request):
    print(request.POST.get("crypto_asset_name"))
    if request.method == "POST":
        try:
            CryptoCurrency.objects.get(CurrencyFullName=request.POST.get("crypto_asset_name"))
        except CryptoCurrency.DoesNotExist:
            return HttpResponseNotFound("<h2>CryptoCurrency not found in our site</h2> "
                                        "<a href="'http://127.0.0.1:8000/accounts/profile/'">Return to profile</a>")
        try:
            crypto_asset = Profile.objects.get(user=request.user).cryptoassets_set.get(crypto_currency_full_name=request.POST.get("crypto_asset_name"))
            crypto_asset.buyinformation_set.create(amount_of_crypto=request.POST.get("crypro_asset_amount"),
                                                   purchase_price=request.POST.get("crypro_asset_purchase_price"))
            crypto_asset.total_number_of_currency += float(request.POST.get("crypro_asset_amount"))

            crypto_asset.save()

        except CryptoAssets.DoesNotExist:
            Profile.objects.get(user=request.user).cryptoassets_set.\
                create(crypto_currency_full_name=request.POST.get("crypto_asset_name"),
                       total_number_of_currency=request.POST.get("crypro_asset_amount")).\
                buyinformation_set.create(amount_of_crypto=request.POST.get("crypro_asset_amount"),
                                          purchase_price=request.POST.get("crypro_asset_purchase_price"))

    return HttpResponseRedirect("http://127.0.0.1:8000/accounts/profile/")

def sell_crypto_assets(request):
    if request.method == "POST":
        try:
            CryptoCurrency.objects.get(CurrencyFullName=request.POST.get("crypto_asset_name"))
        except CryptoCurrency.DoesNotExist:
            return HttpResponseNotFound("<h2>CryptoCurrency not found in our site</h2> "
                                        "<a href="'http://127.0.0.1:8000/accounts/profile/'">Return to profile</a>")

        crypto_asset = Profile.objects.get(user=request.user).cryptoassets_set.get(crypto_currency_full_name=request.POST.get("crypto_asset_name"))
        crypto_asset.soldinformation_set.create(amount_sold_crypto=request.POST.get("crypro_asset_amount"),sold_price=request.POST.get("crypro_asset_purchase_price"))
        crypto_asset.total_number_of_currency -= float(request.POST.get("crypro_asset_amount"))
        crypto_asset.save()

    return HttpResponseRedirect("http://127.0.0.1:8000/accounts/profile/")


