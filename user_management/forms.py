import re
from django import forms
from .models import *

class Register_Form(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "class": "form-control form-control-xl",
        "placeholder": "Nama Pemilik Rekening",
        "required":True
    }))
    ref_code = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "class": "form-control form-control-xl",
        "placeholder": "Kode Referal",
        "required": True
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "class": "form-control form-control-xl",
        "placeholder": "Username",
        "required": True
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "type": "email",
        "class": "form-control form-control-xl",
        "placeholder": "Email",
        "required": True
    }))
    nama_bank = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        "class": "form-control form-control-xl",
        "placeholder": "Nama Bank",
        "required": True
    }))
    no_rekening = forms.CharField(max_length=20,widget=forms.NumberInput(attrs={
        "class": "form-control form-control-xl",
        "placeholder": "Nomor Rekening",
        "required": True
    }))
    phone = forms.CharField(max_length=18,widget=forms.NumberInput(attrs={
        "class": "form-control form-control-xl",
        "placeholder": "Nomor Telfon",
        "required": True
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control form-control-xl",
        "placeholder": "Password",
        "required": True
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control form-control-xl",
        "placeholder": "Ulangi Password",
        "required": True
    }))

    def clean_username(self):
        obj = self.cleaned_data['username']
        if User.objects.filter(username__iexact=obj).exists():
            raise forms.ValidationError("Username sudah digunakan")

        if len(obj) <= 5:
            raise forms.ValidationError("Username harus lebih dari 5 karakter")

        return obj

    def clean_email(self):
        obj = self.cleaned_data['email']
        if Data_User.objects.filter(email__iexact=obj).exists():
            raise forms.ValidationError("Email sudah digunakan")

        return obj

    def clean_ref_code(self):
        obj = self.cleaned_data['ref_code']
        if Data_User.objects.filter(referal_code=obj).exists() == False:
            raise forms.ValidationError("Kode Referal tidak ditemukan")
        return obj

    def clean_no_rekening(self):
        obj = self.cleaned_data['no_rekening']
        if Data_User.objects.filter(no_rekening=obj).exists():
            raise forms.ValidationError("Nomor Rekening sudah digunakan")

        return obj

    def clean_phone(self):
        obj = self.cleaned_data['phone']
        if Data_User.objects.filter(phone=obj).exists():
            raise forms.ValidationError("Nomor Telepon sudah digunakan")

        return obj

    def clean_password1(self):
        obj = self.cleaned_data['password1']
        if re.search('[A-Z]', obj) == None \
                or re.search('[0-9]', obj) == None \
                or re.search('[^A-Za-z0-9]', obj) == None or len(obj) < 8:
            raise forms.ValidationError(
                "Password Harus mengandung 1 Huruf Besar, 1 Angka, dan 1 Symbol. Minimal 8 Karakter")
        return obj

    def clean_password2(self):
        obj = self.cleaned_data['password2']
        if re.search('[A-Z]', obj) == None \
                or re.search('[0-9]', obj) == None \
                or re.search('[^A-Za-z0-9]', obj) == None or len(obj) < 8:
            raise forms.ValidationError(
                "Password Harus mengandung 1 Huruf Besar, 1 Angka, dan 1 Symbol. Minimal 8 Karakter")
        return obj

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password1') != cleaned_data.get('password2'):
            raise forms.ValidationError("Password tidak sesuai")
