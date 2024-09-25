from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('PL','PLIAN'),
        ('EL','ELACHI'),
    ]
    name = models.CharField( max_length=100)
    image = models.ImageField( upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    price = models.CharField(default='0', max_length=20)
    discount = models.IntegerField(default=0, max_length=3)
    def __str__(self) :
        return self.name
    
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField
    comment = models.TextField()
    date_addded = models.DateTimeField(default=timezone.now)
    def __str__(self) :
        return f'{self.user.username} review for {self.chai.name}'
    
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varaities = models.ManyToManyField(ChaiVariety,related_name='stores')
    def __str__(self) :
        return self.name
    
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField()
    
    def __str__(self) :
        return f'Certificate for {self.chai.name}'