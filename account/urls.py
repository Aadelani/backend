from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.TokenObtainPairView.as_view(), name='login'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.user_profile, name='get_user_profile'),
    path('fund-wallet/', views.wallet_deposit, name='wallet_deposit'),
]