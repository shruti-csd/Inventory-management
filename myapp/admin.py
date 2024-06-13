from django.contrib import admin
from .forms import *
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['Productname','Productqnt','Unitoffprd']
    forms=KitchenStockform
    search_fields=['Productname','Unitoffprd']
    
    
admin.site.register(KitchenInventory,UserAdmin)

