from django.urls import path

from . import views

urlpatterns = [
   path('',views.CryptoView.as_view(),name = 'Crypto')
]