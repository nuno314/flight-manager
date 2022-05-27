from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Flight list
    path('flight/list/', views.flightList, name='flight_list'),
    path('flight/detail/<str:pk>/', views.flightDetail, name='flight_detail'),
    path('flight/update/<str:pk>', views.flightUpdate, name='flight_update'),
    path('flight/detailupdate/<str:pk>/', views.flightDetailUpdate, name='flight_detail_update'),   #update flight detail
    path('flight/create/', views.flightCreate, name='flight_create'),
    path('flight/detailcreate/', views.flightDetailCreate, name='flight_detail_create'),   #create detail
    path('flight/delete/<str:pk>', views.flightDelete, name='flight_delete'),



    path('customer/', views.customer),

    # Authentication
    path('signup/', views.signup, name='auth.signup'),
    path('login/', views.login, name='auth.login'),

    # Report
    path('report/', views.report, name='report'),
]