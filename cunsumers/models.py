from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Consumer(models.Model):
    name = models.CharField(max_length=55)
    title  =  models.CharField(max_length=55)
    commission = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name