from django.db import models

# Create your models here.
class Product(models.Model):
    pname=models.CharField(max_length=150,default=True)
    pdescription=models.TextField(max_length=200,default=True)
    pprice=models.DecimalField(max_digits=4,decimal_places=2)
    def __str__(self):
        return self.pname