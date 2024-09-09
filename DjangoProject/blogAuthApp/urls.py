from django.urls import path 
from . import views

urlpatterns = [
    path('register', views.register, name='auth-register'),
    path('login',views.loginUser,name="auth-login"),
    path('logout',views.logoutUser,name="auth-logout"),
]