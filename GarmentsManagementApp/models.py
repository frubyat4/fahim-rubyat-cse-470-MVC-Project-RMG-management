from django.contrib.auth.models import User
from django.db import models


class Garment(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    product_id = models.IntegerField(unique=True,default=-1)
    current_stock = models.IntegerField(null=True)
    garment = models.ForeignKey(Garment,on_delete=models.CASCADE,null=True)
    Name=models.CharField(max_length=20)
    price = models.fields.PositiveIntegerField()
    description = models.CharField(max_length=200)
    workingHoursPerItem = models.IntegerField(null=True)

    def __str__(self):
        return self.Name

class Department(models.Model):
    Name = models.CharField(max_length=15)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=1000, null=True)
    note = models.CharField(max_length=3000, null=True)

    def __str__(self):
        return self.Name

class Deparment_Admin(models.Model):
    user_ref = models.OneToOneField(User,on_delete=models.CASCADE)
    Department = models.ForeignKey(Department,on_delete=models.CASCADE)
    role = models.CharField(max_length=20)



class Employee(models.Model):
    EmployeeID = models.IntegerField(unique=True,default=-1)
    Name = models.CharField(max_length=20)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField()
    Phone = models.CharField(max_length=12,null=True)
    address = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length= 20,null=True)

    def __str__(self):
        return self.department

class Order(models.Model):
    OrderID = models.IntegerField(unique=True,default=-1)
    Status = models.CharField(max_length= 20,null=True)
    CustomerName = models.CharField(max_length=20)
    CustomerPhn = models.CharField(max_length=12)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    TotalPrice = models.BigIntegerField()

    def __str__(self):
        return str(self.OrderID)

class Shipments(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    delivaryDate = models.DateField()

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    Company_Name = models.CharField(max_length=200)
    Company_Address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=12, null=True)
    garment = models.ForeignKey(Garment, on_delete=models.CASCADE, null=True)
    deliveryDate = models.DateField()

    def __str__(self):
        return self.garment