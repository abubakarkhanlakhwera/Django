from django.urls import path
from . import views

urlpatterns = [
    path('home',views.all_chai,name="all_chai"),  
    path('home/chai/<int:chai_id>/',views.chai_detail,name='chai_detail'),
    path('home/price/<int:price_id>/',views.Price,name='Price'),
        
]
