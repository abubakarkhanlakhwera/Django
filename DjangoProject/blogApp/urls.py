from django.urls import path 
from . import views

urlpatterns = [
    path('',views.Home, name='blog-homepage'),
    path('about/',views.About, name='blog-about'),
]


