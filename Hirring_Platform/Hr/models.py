from django.contrib.auth.models import User
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    posted_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class HRProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hr_profile')
    full_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    position_title = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField
    company_website = models.URLField(blank=True,null=True)
    linkedin_profile = models.TextField(blank=True,null=True)
    bio = models.TextField(blank=True,null=True)

    def __str__(self) :
        return f"{self.full_name} - {self.company_name}"