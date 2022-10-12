from django.urls import path

from . import views
app_name = 'crypto'
urlpatterns = [
   path('',views.CryptoView,name = 'Crypto'),
   path('<str:pk>/',views.DetailView,name='crypto_detail')
]