from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.hr_signup, name='signup'),  # Add this line
    path('dashboard/', views.hr_dashboard, name='hr_dashboard'),
    path('post-job/', views.post_job, name='post_job'),
    # path('candidate/', views.candidate_dashboard, name='candidate_dashboard'),
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('', views.hr_home, name='hr_home'),  # Adjusted name for the home page
    path('accounts/login/', auth_views.LoginView.as_view(), name='signin'),
]