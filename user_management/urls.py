from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

urlpatterns = [
    path('register/',registerView,name='register'),
    path('login/',loginView,name='login'),
    path('logout/',login_required(logoutView,login_url='login'),name='logout'),
    path('',login_required(dashboardView,login_url='login'),name='dashboard'),
    path('profile/',login_required(profielView,login_url='login'),name='profile'),
    path('history-invest/',login_required(historyInvestView,login_url='login'),name='history-invest'),
    path('history-penarikan/',login_required(historyPenarikan,login_url='login'),name='history-penarikan'),
    path('history-pembayaran/', login_required(historyPembayaran,login_url='login'), name='history-pembayaran'),
    path('teams/<int:level>/',login_required(teamsView,login_url='login'),name='teams')
]