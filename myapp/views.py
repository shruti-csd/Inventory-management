from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.db.models import Max, Min



def home(request):
    # Calculate min and max quantities
    min_quantity = KitchenInventory.objects.aggregate(Min('Productqnt'))['Productqnt__min']
    max_quantity = KitchenInventory.objects.aggregate(Max('Productqnt'))['Productqnt__max']

    # Extract top 3 products
    top_products = KitchenInventory.objects.order_by('-Productqnt')[:3]

    context = {
        'min_quantity': min_quantity,
        'max_quantity': max_quantity,
        'top_products': top_products
    }
    return render(request, 'myapp/home.html', context)
 
def aboutus(request):
    return render(request,'myapp/aboutus.html')

def contactus(request):
    return render(request,'myapp/contactus.html')


def kitcheninv(request):
    form = SearchInventory(request.POST or None)
    queryset = KitchenInventory.objects.all()
    context = {
        'forms': form,
        'queryset': queryset
    }
    if request.method == "POST":
        if form.is_valid():
            product_name = form.cleaned_data.get('Productname')
            product_quantity = form.cleaned_data.get('Productqnt')
            # Filter queryset based on form inputs
            queryset = KitchenInventory.objects.filter(Productname__icontains=product_name, Productqnt__icontains=product_quantity)
            context = {
                'forms': form,
                'queryset': queryset
            }
    return render(request, 'myapp/kitcheninv.html', context)



def addinventory(request):
    form=KitchenStockform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('kitchen')
    
    context={
        'form':form
    }
    return render(request,'myapp/addinv.html',context)

def showonventory(request):
    queryset=KitchenInventory.objects.all()
    context={
        'queryset':queryset
    }
    
    return render(request,'myapp/showdata.html',context)

def delete(request, pk):
    queryset=KitchenInventory.objects.get(id=pk)
    if request.method=='POST':
        queryset.delete()
        return redirect('kitchen')
    return render(request,'myapp/delete.html',{'queryset':queryset})

def update(request,pk):
    queryset=KitchenInventory.objects.get(id=pk)
    form=UpdateInventory(instance=queryset)
    if request.method=='POST':
        form=UpdateInventory(request.POST,instance=queryset)
        if form.is_valid():
         form.save()
         return redirect('kitchen')
    context={
        'form':form
    }
    
    return render(request,'myapp/addinv.html',context)
    

