from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.aboutus,name='about'),
    path('contact',views.contactus,name='contact'),
    path('kitchen',views.kitcheninv,name='kitchen'),
    path('add/',views.addinventory,name='add'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('update/<str:pk>/',views.update,name='update'),
    path('showdata/',views. showonventory,name='datashow')
   
]
   