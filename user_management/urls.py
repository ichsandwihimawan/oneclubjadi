from django.urls import path
from .views import *


urlpatterns = [
    path('register/',registerView,name='register'),
    path('login/',loginView,name='login'),
    path('logout/',logoutView,name='logout'),
    path('',dashboardView,name='dashboard'),
    path('profile/',profielView,name='profile'),
    path('history-invest/',historyInvestView,name='history-invest'),
    path('history-penarikan/',historyPenarikan,name='history-penarikan'),
    path('history-pembayaran/', historyPembayaran, name='history-pembayaran'),
    path('teams/<int:level>/',teamsView,name='teams')
]