from django.db import models

class Register(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    cpf = models.CharField(max_length=11)
    
    def __str__(self):
        return self.username