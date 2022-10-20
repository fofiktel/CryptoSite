from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'

urlpatterns = [
   path('register/',views.register,name = 'register'),
   path('profile/', views.profile, name='profile'),
   path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
   path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
   path('add_favorite_crypto/',views.add_favorite_cryptocurrency,name="add_favorite_crypto"),
   path('remove_favorite_crypto/<str:pk>',views.delete_favorite_cryptocurrency,name='delete_favorite_crypto'),
]

