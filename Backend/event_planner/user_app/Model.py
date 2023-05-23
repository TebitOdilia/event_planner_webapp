from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    contact = models.IntegerField(blank=True, null=True)
    
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
class Event(model.Model):
    event_id = models.IntegerField(unique=True)
    name = models.CharField(max_length= 255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    username= models.ForiegnKey(User, on_delete=models.SET_NULL,null=True)
    budget = models ForiegnKey(Budget, on_delete=models.CASCADE, default=0)
    report_id = models.ForeignKey(Report, on_ delete=models.SET_NULL, null=True)
    def_str_(self):
        return self.name
