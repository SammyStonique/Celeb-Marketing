from django.db import models

# Create your models here.

class CustomerRegistration(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    password = models.CharField(max_length = 30)
    confirm_password = models.CharField(max_length = 30)