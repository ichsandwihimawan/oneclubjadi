from django.urls import path
from .views import *

urlpatterns = [
    path('invest/',investUser,name='invest'),
    path('deposit/',depositView,name='deposit'),
    path('withdraw/',withdrawView,name='withdraw'),
    path('rincian-roi/',rincianBonusRoiView,name='rincian-roi')
]