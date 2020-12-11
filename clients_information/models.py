from django.db import models
from datetime import datetime
# Create your models here.

class Policy_Type(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title
        
class Client(models.Model):
    fullname = models.CharField(max_length=30)
    sum_insured = models.FloatField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    policy_type = models.ForeignKey(Policy_Type,on_delete=models.CASCADE)

    @property
    def age(self):
        return int((datetime.now().date() - self.dob).days / 365.25)