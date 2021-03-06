from django.db.models import Sum
from transaction.models import *

def globalContext(request):
    if request.user.is_authenticated:
        context = {
            'modal': Invest.objects.filter(user=request.user.data_user,is_balik_modal=False).aggregate(Sum('nominal'))[
                'nominal__sum'] if Invest.objects.filter(user=request.user.data_user,is_balik_modal=False).exists() else 0,
            'test':Invest.objects.filter(user=request.user.data_user,is_balik_modal=False).exists()
        }
        return context
    return {}