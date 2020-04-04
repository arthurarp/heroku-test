from django.db import models
from login.models import Register

class Item(models.Model):
    name = models.CharField(max_length=30, null=False)
    where = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=30, null=True)
    user = models.ForeignKey(Register, on_delete=models.CASCADE, null=False)


    def __str__(self):
        return self.name
