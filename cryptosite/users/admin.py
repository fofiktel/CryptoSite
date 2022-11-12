from django.contrib import admin

from .models import Profile,CryptoAssets,BuyInformation

admin.site.register(Profile)
admin.site.register(CryptoAssets)
admin.site.register(BuyInformation)