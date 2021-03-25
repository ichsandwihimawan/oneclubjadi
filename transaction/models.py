from django.db import models
from user_management.models import *

# Create your models here.

class Jenis_Invest(models.Model):
    jenis = models.CharField(max_length=50)

    def __str__(self):
        return self.jenis

class Invest(models.Model):
    user = models.ForeignKey(Data_User,on_delete=models.CASCADE,null=True,blank=True)
    jenis = models.ForeignKey(Jenis_Invest,on_delete=models.CASCADE,null=True,blank=True)
    nominal = models.FloatField(null=True,blank=True)
    modal = models.FloatField(null=True,blank=True)
    roi = models.FloatField(null=True,blank=True,default=0)
    roi_count = models.FloatField(null=True,blank=True,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    next_payment = models.DateTimeField(null=True,blank=True)
    withdraw_pay = models.FloatField(null=True,blank=True,default=0)
    end_at = models.DateTimeField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_balik_modal=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} {self.nominal}'

class Deposit(models.Model):
    via_bank = models.CharField(max_length=20,null=True,blank=True)
    user = models.ForeignKey(Data_User,on_delete=models.CASCADE,null=True,blank=True)
    nominal = models.FloatField(null=True,blank=True)
    nama_bank = models.CharField(max_length=20,null=True,blank=True)
    nama_pemilik_rekening = models.CharField(max_length=100,null=True,blank=True)
    no_rekening = models.FloatField(null=True,blank=True)
    status = models.BooleanField(null=True,blank=True,default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.nominal}'

class Bonus_Generasi(models.Model):
    for_user = models.ForeignKey(Data_User,on_delete=models.CASCADE,null=True,blank=True,related_name='sender')
    from_user = models.ForeignKey(Data_User,on_delete=models.CASCADE,null=True,blank=True)
    bonus = models.FloatField(null=True,blank=True)
    generasi = models.FloatField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.for_user} {self.bonus} {self.generasi}'

class Bonus_Roi(models.Model):
    invest = models.ForeignKey(Invest,on_delete=models.CASCADE,null=True,blank=True)
    roi = models.FloatField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.invest.user} {self.roi}'

class Weekly_Withdraw(models.Model):
    invest = models.ForeignKey(Invest,on_delete=models.CASCADE,null=True,blank=True)
    nominal = models.FloatField(null=True,blank=True)
    status = models.BooleanField(null=True,blank=True,default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.invest.user} {self.nominal}'

class Afiliasi_Withdraw(models.Model):
    user = models.ForeignKey(Data_User,on_delete=models.CASCADE,null=True,blank=True)
    nominal = models.FloatField(null=True,blank=True)
    status = models.BooleanField(null=True,blank=True,default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.nominal} {self.status}'






