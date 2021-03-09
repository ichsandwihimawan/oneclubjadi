from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel,TreeForeignKey
# Create your models here.

class Data_User(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=100,null=True,blank=True)
    referal_code = models.CharField(max_length=10,null=True,blank=True, unique=True)
    email = models.EmailField(null=True,blank=True, unique=True)
    user_rel = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    referal_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    nama_bank = models.CharField(max_length=100,null=True,blank=True)
    no_rekening = models.CharField(max_length=50,null=True,blank=True,unique=True)
    phone = models.CharField(max_length=16,null=True,blank=True,unique=True)
    balance = models.FloatField(null=True,blank=True,default=0)
    bonus_afiliasi = models.FloatField(null=True,blank=True,default=0)
    roi = models.FloatField(null=True,blank=True,default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
