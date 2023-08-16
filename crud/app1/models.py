from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Login(AbstractUser):
    is_trainer = models.BooleanField(default=False)
    name = models.CharField(max_length=25, null=True)
    age = models.IntegerField(null=True)
    address = models.TextField(null=True)
    contact_no = models.IntegerField(null=True)

    def __str__(self):
        return self.name
