from django.shortcuts import render,get_object_or_404

from .models import CryptoCurrency
from django.views import generic
from django.urls import reverse


class CryptoView(generic.ListView):
    template_name = 'crypto/CryptoList.html'

    context_object_name = 'crypto_list'

    def get_queryset(self):
        return CryptoCurrency.objects.all()
# Create your views here.
