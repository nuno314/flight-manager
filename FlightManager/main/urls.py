from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flights/', views.flights, name='flights'),
    path('customer/', views.customer, name='customer'),

    # Airport
    path('airport/list/', views.airport_list, name='airport_list'), 
    path('airport/create/', views.createAirport, name='create_airport'),
]