from xmlrpc.client import DateTime
from django.db import models

# Create your models here.
import datetime

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    expiration_date = models.DateField()
   # duration =(expiration_date-DateTime.date.today())/datetime.timedelta(days=1)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    #分两个表
    def is_expired(self):
        return self.expiration_date < datetime.date.today()

    def is_close_to_expire(self, days=1):
        #return datetime.date.today() + datetime.timedelta(days=days) >= self.expiration_date > datetime.date.today()
        return datetime.date.today() + datetime.timedelta(days=days) >= self.expiration_date

