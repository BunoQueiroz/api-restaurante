from django.db import models
from django.contrib.auth.models import User

class Client(User):
    image = models.ImageField(upload_to='clients/%Y/%m/%d')
    cpf = models.CharField(max_length=11, default='00000000000')

    def __str__(self):
        return self.first_name
