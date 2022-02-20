from django.urls import path
# from django.urls.resolvers import URLPattern
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


app_name='accounts'

urlpatterns  = [

path('', views.doctors_list, name='doctors_list'),
path('login/',views.user_login, name='login' ),
path('myprofile/' , views.myprofile, name = 'myprofile'),
path('update_profile/', views.updat_profile , name= 'update_profile' ),
path('signup/', views.signup , name='signup'),
path('<slug:slug>/', views.doctor_detail, name='doctor_detail'),



]