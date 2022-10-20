from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .forms import UserRegisterForm


from .models import Profile
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


@login_required
def profile(request):

    user_profile = get_object_or_404(Profile, user=request.user)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'users/profile.html', context)


def add_favorite_cryptocurrency(request):
    try:
        user_profile = get_object_or_404(Profile, user=request.user)
    except Profile.DoesNotExist:
        return HttpResponseNotFound("<h2>Profile not found</h2>")

    if request.method == "POST":
        try:
            user_profile.crypto.add(CryptoCurrency.objects.get(CurrencyFullName=request.POST.get("cryptocurrency_name")))
            user_profile.save()
        except CryptoCurrency.DoesNotExist:
            return HttpResponseNotFound("<h2>CryptoCurrency not found</h2> <a href="'http://127.0.0.1:8000/accounts/profile/'">Return to profile</a>")
    return HttpResponseRedirect("http://127.0.0.1:8000/accounts/profile/")


def delete_favorite_cryptocurrency(request, pk):
    user_profile = get_object_or_404(Profile, user=request.user)
    user_profile.crypto.remove(CryptoCurrency.objects.get(currency_id=pk))
    return HttpResponseRedirect("http://127.0.0.1:8000/accounts/profile/")
