from django.urls import path
from userapp import views

urlpatterns = [
    path('',views.user,name="register")


]