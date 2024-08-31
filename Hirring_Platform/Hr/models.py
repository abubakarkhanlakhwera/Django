from django.contrib.auth.models import User
from django.db import models

class HRProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hr_profile')
    full_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    position_title = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    company_website = models.URLField(blank=True, null=True)
    linkedin_profile = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.company_name}"

class Job(models.Model):
    hr_profile = models.ForeignKey(HRProfile, on_delete=models.CASCADE)
    candidate = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    posted_on = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
