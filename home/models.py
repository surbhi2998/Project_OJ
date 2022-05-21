from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,PermissionsMixin)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password,**kwargs):
        user = User.objects.create(email=self.normalize_email(email),**kwargs)
        user.set_password(password) # password will notget stored in db django will authenticate through method checkpassword
        user.save()
        return user
    def create_superuser(self,email,password): # we override createuser and super user methods beacuse username field has changed to email
        user = self.create_user(email,password)
        user.isAdmin = True
        user.is_staff=True
        user.is_superuser=True
        user.save()
        return user

class User(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=100)
   # userId = models.IntegerField(primary_key=True,unique=True) # by default django makes id in evry table, Primary key
    email = models.EmailField(max_length=255,unique=True)
    #password = models.CharField(max_length=100)
    is_staff=models.BooleanField(default=False)
    rank=models.IntegerField(default=0)
    problemSolved = models.IntegerField(default=0)
    isAdmin= models.BooleanField(default=False) # field will be not be in form but in db

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects=UserManager()


class Problems(models.Model):
    problemStatement = models.TextField(max_length=5000)
    name=models.TextField(max_length=100)
    CATEGORY =(
        ('EASY',('Easy')),
        ('MEDIUM',('Medium')),
        ('HARD',('Hard')),
    )
    category=models.CharField(max_length=32,choices=CATEGORY) 

class Solutions(models.Model):
    problemId=models.ForeignKey(Problems, on_delete=models.CASCADE)
    VERDICT = (
        ('RUN TIME ERROR', ('Run Time Error')),
        ('COMPILE TIME ERROR',('Compile Time Error')),
        ('TIME LIMIT EXCEEDED',('Time Limit Exceeded')),
        ('ACCEPTED',('Accepted')), # TCno failed needs to be added
    )
    verdict=models.CharField(max_length=50,choices=VERDICT,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    submitted_date=models.DateTimeField(auto_now=True)
    language=models.CharField(max_length=50,default="a")
    code=models.TextField(default="a")


    unique_together=["submitted_date",]

class TestCases(models.Model):
    input = models.CharField(max_length=100)
    output = models.CharField(max_length=100)
    problemId=models.ForeignKey(Problems,on_delete=models.CASCADE)

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    desc=models.TextField()


#sample model class
class Items(models.Model):
    name = models.TextField(max_length=200)
    price = models.TextField(max_length=50)
    description = models.TextField(max_length=500,null=True)
