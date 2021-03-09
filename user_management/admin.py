from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin,MPTTModelAdmin
from .models import *
# Register your models here.

admin.site.register(Data_User,DraggableMPTTAdmin)
