from django.db import models

class Member(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    passwd = models.CharField(max_length=50)
    age = models.IntegerField(max_length=3)

    def __str__(self):
        return  self.fname +   '' + self.lname