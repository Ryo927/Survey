from django.db import models


# Create your models here.


class Data(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    income = models.CharField(max_length=50)
    edu = models.CharField(max_length=50)

    def __str__(self):
        return self.name +' - '+ self.email