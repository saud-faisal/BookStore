from django.db import models

# Create your models here.
class regData(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    college_roll=models.IntegerField()
    batch=models.CharField(max_length=80,default='none')
    branch=models.CharField(max_length=50,default='none')
    email=models.EmailField()
    password=models.IntegerField()
    cpassword=models.IntegerField()
class Books(models.Model):
    bookname=models.CharField(max_length=50)
    authorname=models.CharField(max_length=50)
    Publication=models.CharField(max_length=50)
    Isbn=models.CharField(max_length=50)
    imag=models.ImageField(upload_to='images',blank=True)
    date=models.DateField()
    time=models.TimeField(auto_now=True)
