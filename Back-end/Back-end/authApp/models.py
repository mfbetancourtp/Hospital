from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('NameProduct', max_length=15, unique=True)
    price = models.IntegerField(default=0)
