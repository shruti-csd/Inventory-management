from django import forms 
from .models import *

class KitchenStockform(forms.ModelForm):
    class Meta:
        model=KitchenInventory
        fields=['Productname','Productqnt','Unitoffprd']
        
        
class SearchInventory(forms.ModelForm):
    class Meta:
        model=KitchenInventory
        fields=['Productname','Productqnt']
        
class UpdateInventory(forms.ModelForm):
    class Meta:
        model=KitchenInventory
        fields=['Productname','Productqnt','Unitoffprd']
        
class IssueForm(forms.ModelForm):
    class Meta:
        model=KitchenInventory
        fields=['Productqnt','Unitoffprd']
        
# class RecieveForm(forms.ModelForm):
#     class Meta:
#         model=KitchenInventory
#         fields=['recieve_quantity']
        
