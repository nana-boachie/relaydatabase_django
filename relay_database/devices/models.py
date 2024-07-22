from django.db import models

# Create your models here.
class Relay(models.Model):
    name=models.CharField( max_length=50)
    AREA_CHOICES=[
        ('accra','Accra'),
        ('tema','Tema')
    ]

    area=models.CharField( max_length=50, choices=AREA_CHOICES)
    set_file=models.FileField( upload_to='setfiles', max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name
    