from django.db import models
from Hr.models import Job
class Candidate(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    skills = models.TextField()
    resume = models.FileField(upload_to='resume/')
    applied_jobs = models.ManyToManyField('Hr.Job',related_name='candidate',blank=True)
    def __str__(self):
        return self.name