from django.urls import path , include
from . import views 
urlpatterns = [
    path('',views.home),
    path('<str:room>/', views.room),
    path('checkview',views.checkview),
    path('send',views.send),
    path('getMessages/<str:room>/',views.getMessages)
]