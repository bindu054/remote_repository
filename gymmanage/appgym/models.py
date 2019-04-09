from django.db import models

# Create your models here.
class Add_plans(models.Model):
    Name=models.CharField(max_length=500,primary_key=True)
    Plan_Description=models.CharField(max_length=500)

class View_suggestion(models.Model):
    suggestion=models.CharField(max_length=500)

class payment(models.Model):
    Payment_type=models.CharField(max_length=500)

# class View_Plans(models.Model):
#     Plan_name=models.ForeignKey(Add_plans,on_delete=models.CASCADE)

class Registration(models.Model):
    Idno=models.IntegerField()
    Name=models.CharField(max_length=500)
    Contact_no=models.IntegerField()
    Age=models.IntegerField()
    Email=models.EmailField(max_length=500,primary_key=True)
    Password=models.CharField(max_length=50)
    Address=models.CharField(max_length=100)

class Sugesstion(models.Model):
    Email=models.ForeignKey(Registration,on_delete=models.CASCADE)
    suggestions=models.CharField(max_length=500,primary_key=True)
    date=models.DateField()

class Password(models.Model):
    email=models.ForeignKey(Registration,on_delete=models.CASCADE)
    password=models.CharField(max_length=50,primary_key=True)