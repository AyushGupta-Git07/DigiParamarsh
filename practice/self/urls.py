from django.urls import path
from . import views

#localhost:8000/chai
#localhost:8000/chai/order
urlpatterns = [
    path('', views.home, name='home'),
    path('all_self/', views.all_self, name='all_self'),
    path('order/', views.order, name='order'),
   
]
