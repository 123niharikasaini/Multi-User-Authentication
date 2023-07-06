from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
   path('',views.index,name="index"),
   path('login/',views.login_view,name="login_view"),
   path('register/',views.register,name="register"),
   path('admin/',views.admin,name="admin"),
   path('customer/',views.customer,name="customer"),
   path('driver/',views.driver,name="driver"),


]