
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('crypto/',include('crypto.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('users.urls'))
]
