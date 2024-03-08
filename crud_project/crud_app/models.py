from django.db import models


# Create your models here.

class Employee(models.Model):
    objects = None
    EmpId = models.CharField(max_length=3)
    EmpName = models.CharField(max_length=100)
    EmpGender = models.CharField(max_length=10)
    EmpEmail = models.EmailField(max_length=200)
    EmpDesignation = models.CharField(max_length=130)

    class Meta:
        db_table = "Employee"
