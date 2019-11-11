from django.db import models

# Create your models here.


class BOOK(models.Model):
    nid=models.AutoField(primary_key=True)
    title =models.CharField(max_length=255)
    memo =models.CharField(max_length=255)

class user1(models.Model):
    name =models.CharField(max_length=255)
