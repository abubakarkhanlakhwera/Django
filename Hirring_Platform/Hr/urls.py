from django.urls import path
from . import views

urlpatterns = [
    path('hr',views.hr,name= 'hr'),
    path('post_job/', views.post_job, name='post_job'),

]