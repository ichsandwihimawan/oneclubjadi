import locale
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from .models import *

# Create your views here.
from rest_framework.response import Response


@api_view(['POST'])
def investUser(request):
    print(request.data)
    user = request.user.data_user
    jenis_inv, created = Jenis_Invest.objects.get_or_create(jenis=request.data.get('jenis'))
    nominal = request.data.get('nominal')
    if user.balance < float(nominal):
        return Response("Balance tidak cukup, silahkan Deposit terlebih dahulu", status=status.HTTP_400_BAD_REQUEST)
    if jenis_inv.jenis == 'star' and float(nominal) < 1000000:
        return Response("Minimal Purchase untuk paket STAR adalah 1.000.000", status=status.HTTP_400_BAD_REQUEST)
    if jenis_inv.jenis == 'vip' and float(nominal) < 100000000:
        return Response("Minimal Purchase untuk paket STAR adalah 100.000.000", status=status.HTTP_400_BAD_REQUEST)
    next_payment = timezone.now() + timezone.timedelta(weeks=1,days=1)
    inv = Invest.objects.create(user=user,
                                jenis=jenis_inv,
                                nominal=float(nominal),
                                next_payment=next_payment,
                                end_at=timezone.now() + timezone.timedelta(weeks=12))
    ances = user.get_ancestors().filter(level__gte=user.level - 3, level__lte=user.level).order_by('-level')
    user.balance -= float(nominal)
    user.save()
    for x in ances:
        if Invest.objects.filter(user=x, is_active=True).exists():
            if jenis_inv.jenis == 'star':
                if user.level - x.level == 1:
                    x.bonus_afiliasi += float(inv.nominal) * 0.05
                    x.save()
                    Bonus_Generasi.objects.create(for_user=x, from_user=user, bonus=float(nominal) * 0.05,
                                                  generasi=user.level - x.level)
                elif user.level - x.level == 2:
                    x.bonus_afiliasi += float(inv.nominal) * 0.03
                    x.save()
                    Bonus_Generasi.objects.create(for_user=x, from_user=user, bonus=float(nominal) * 0.03,
                                                  generasi=user.level - x.level)
                elif user.level - x.level == 3:
                    x.bonus_afiliasi += float(inv.nominal) * 0.02
                    x.save()
                    Bonus_Generasi.objects.create(for_user=x, from_user=user, bonus=float(nominal) * 0.02,
                                                  generasi=user.level - x.level)
            elif jenis_inv.jenis == 'vip':
                if user.level - x.level == 1:
                    x.bonus_afiliasi += float(inv.nominal) * 0.03
                    x.save()
                elif user.level - x.level == 2:
                    x.bonus_afiliasi += float(inv.nominal) * 0.01
                    x.save()
                elif user.level - x.level == 3:
                    x.bonus_afiliasi += float(inv.nominal) * 0.01
                    x.save()

    return Response("Purchase Berhasil dilakukan, Silahkan tunggu Profit anda berjalan :)", )


@api_view(['POST'])
def depositView(request):
    user = request.user.data_user
    print(request.data)
    if request.data.get('nominal') == '' or request.data.get('nama_bank') == '' or request.data.get(
            'nama_pemilik_rekening') == '' or request.data.get('nominal') == '' or request.data.get(
        'no_rekening') == '' or request.data.get('nominal') == '':
        return Response("Harap isi form yang kosong", status=status.HTTP_400_BAD_REQUEST)
    if Deposit.objects.filter(user=user, status=None).exists():
        return Response("Kamu masih memiliki deposit yang pending, silahkan tunggu beberapa saat",
                        status=status.HTTP_400_BAD_REQUEST)

    Deposit.objects.create(user=user,
                           nominal=request.data.get('nominal'),
                           nama_bank=request.data.get('nama_bank'),
                           nama_pemilik_rekening=request.data.get('nama_pemilik_rekening'),
                           no_rekening=request.data.get('no_rekening'),
                           via_bank=request.data.get('via_bank')
                           )
    return Response('Deposit Sukses, Mohon tunggu admin melakukan konfirmasi')

@api_view(['POST'])
def withdrawView(request):
    print(request.data)
    user = request.user.data_user
    if user.bonus_afiliasi < float(request.data.get('nominal')):
        return Response('Bonus afiliasi tidak cukup', status=status.HTTP_400_BAD_REQUEST)
    Afiliasi_Withdraw.objects.create(user=user, nominal=float(request.data.get('nominal')))
    user.bonus_afiliasi -= float(request.data.get('nominal'))
    user.save()
    return Response("Withdraw anda sedang di proses. mohon tunggu beberapa saat")

@api_view(['GET'])
def rincianBonusRoiView(request):
    user =request.user.data_user
    dt_roi = Bonus_Roi.objects.filter(invest__user=user).order_by('-id')
    dt = {}
    temp = []
    for x,y in enumerate(dt_roi):
        temp.append([
            x+1,
            'Rp. {:20,.2f}'.format(y.invest.nominal),
            y.invest.jenis.jenis.upper(),
            'Rp. {:20,.2f}'.format(y.roi),
            y.created_at.strftime("%d-%m-%Y")
        ])
    dt['data'] = temp
    return Response(dt)

