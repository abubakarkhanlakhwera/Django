from django.urls import path
from . import views

urlpatterns = [
    path('candidate',views.candidate_dashboard, name='candidate_dashboard'),
     path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job')
]