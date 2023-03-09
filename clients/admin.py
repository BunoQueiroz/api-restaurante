from django.contrib import admin
from clients.models import Account, Client, Order, Product

admin.site.register(Account)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Product)
