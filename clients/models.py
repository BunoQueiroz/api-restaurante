from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Client(User):
    image = models.ImageField(upload_to='clients/%Y/%m/%d')
    cpf = models.CharField(max_length=11, default='00000000000')

    def __str__(self):
        return self.first_name

class Product(models.Model):
    name = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=150, blank=True)
    price = models.CharField(max_length=10, blank=False)
    date_create = models.DateField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(blank=True, upload_to='products/%Y/%m/%d')

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    amount = models.CharField(max_length=2, blank=None, default='1')
    time = models.DateTimeField(default=timezone.now)

class Account(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
