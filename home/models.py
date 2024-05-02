from django.db import models

# Create your models here.

class Applicant(models.Model):
    id = models.BigAutoField(primary_key=True)
    reg_no = models.CharField(max_length=15, unique=True)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=500)
    email = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=13)
    last_login = models.DateTimeField


class Examiner(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=500)
    email = models.CharField(max_length=50, unique=True)
    subject = models.CharField(max_length=50)


class Admin(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=500)
    email = models.CharField(max_length=50)
