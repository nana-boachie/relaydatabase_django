from django.db import models

# Create your models here.

class Relay(models.Model):
    relay_name = models.CharField(max_length=30)

    RELAY_CHOICES =[
        ('sel' ,'SEL'),
        ('micom','MiCOM')
    ]
    manufacturer = models.CharField( choices=RELAY_CHOICES,default='sel',max_length=30)

    def get_full_name(self):
      return f"{self.relay_name}{self.manufacturer}"


    def __str__(self):
        return self.relay_name
