from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
class Department(models.Model):
    name = models.CharField(max_length = 150)
    description = models.TextField(blank = True)
    created_at = models.DateField()

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=150)
    department = models.OneToOneField(Department, on_delete = models.CASCADE, null=True, blank=True, default="Employee")
    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField()
    role = models.ForeignKey(Role, on_delete = models.CASCADE)
    phone_num = models.IntegerField(validators = [MaxValueValidator(9999999999), MinValueValidator(9)])
    joined_date = models.DateField()
    address = models.TextField()
    department  = models.ForeignKey(Department, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name