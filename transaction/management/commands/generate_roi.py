from django.core.management.base import BaseCommand
from django.utils import timezone
from transaction.models import *

class Command(BaseCommand):
    help = 'Generate Roi'

    def handle(self, *args, **kwargs):
        all_active_invest = Invest.objects.filter(end_at__date__gte=timezone.now().date())
        for x in all_active_invest:
            bonus = x.nominal - (x.nominal * 0.1)
            if x.jenis.jenis == 'star':
                bonus = bonus * 0.0075
                Bonus_Roi.objects.create(invest=x,roi=bonus)
                x.user.roi+=bonus
                x.user.save()
                x.roi+=bonus
                x.roi_count+=1
                x.save()
                print(f'generated roi for {x.user.user_rel.username} of {bonus}')
            elif x.jenis.jenis == 'vip':
                bonus = bonus * 0.01
                Bonus_Roi.objects.create(invest=x,roi=bonus)
                x.user.roi+=bonus
                x.user.save()
                x.roi+=bonus
                x.roi_count+=1
                x.save()
                print(f'generated roi for {x.user.user_rel.username} of {bonus}')
