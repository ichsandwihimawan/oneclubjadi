from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.db.models import Sum
from django.shortcuts import render, redirect
from .forms import *
from transaction.models import *
from django.utils.crypto import get_random_string


# Create your views here.

def registerView(request):
    form = Register_Form()
    if request.method == 'POST':
        form = Register_Form(data=request.POST)
        if form.is_valid():
            ref_code = f'OC{get_random_string(length=8).upper()}'
            ref_by = Data_User.objects.get(referal_code=form.cleaned_data['ref_code'])
            us = User.objects.create_user(username=form.cleaned_data['username'],
                                          password=form.cleaned_data['password1'])
            Data_User.objects.create(user_rel=us,
                                     name=form.cleaned_data['name'],
                                     referal_code=ref_code,
                                     referal_by=ref_by,
                                     parent=ref_by,
                                     email=form.cleaned_data['email'],
                                     nama_bank=form.cleaned_data['nama_bank'],
                                     no_rekening=form.cleaned_data['no_rekening'],
                                     phone=form.cleaned_data['phone'],
                                     )
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'auth-register.html', context)


def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Username atau Password Salah!')
        return redirect('login')
    return render(request, 'auth-login.html')


def logoutView(request):
    logout(request)
    return redirect('login')


def dashboardView(request):
    user = request.user.data_user
    context = {
        'total_star': Invest.objects.filter(is_active=True, jenis__jenis='star',user=user).aggregate(
            Sum('nominal'))['nominal__sum'] if Invest.objects.filter(is_active=True, jenis__jenis='star',user=user).exists() else 0,
        'total_vip': Invest.objects.filter(is_active=True, jenis__jenis='vip',user=user).aggregate(
            Sum('nominal'))['nominal__sum'] if Invest.objects.filter(user=user,is_active=True, jenis__jenis='vip').exists() else 0,
        'bonus_afiliasi': user.bonus_afiliasi,
        'roi': user.roi,
        'total_bonus': user.roi + user.bonus_afiliasi,
    }
    return render(request, 'index.html', context)

def profielView(request):

    return render(request,'profile.html')

def historyInvestView(request):
    all_invest = Invest.objects.filter(user=request.user.data_user).order_by('-id')

    context = {
        'dt_invest': all_invest
    }
    return render(request,'history_invest.html',context)

def historyPenarikan(request):
    dt_penarikan = Afiliasi_Withdraw.objects.filter(user=request.user.data_user).order_by('-id')
    context = {
        'dt_penarikan':dt_penarikan
    }
    return render(request,'history_penarikan.html',context)

def historyPembayaran(request):
    dt_pembayaran = Weekly_Withdraw.objects.filter(invest__user=request.user.data_user).order_by('-id')
    context = {
        'dt_pembayaran':dt_pembayaran
    }
    return render(request,'history_pembayaran.html',context)

def teamsView(request,level):
    user = request.user.data_user
    us_level = user.level + level if level <= 3 else user.level + 1
    dt_team = user.get_descendants().filter(level=us_level)
    for x in dt_team:
        tp = Invest.objects.filter(user=x,is_active=True).aggregate(Sum('nominal'))['nominal__sum'] if Invest.objects.filter(user=x,is_active=True).exists() else 0
        x.total_purchase = tp
    context = {
        'dt_team':dt_team,
        'level':level
    }
    return render(request,'teams.html',context)


