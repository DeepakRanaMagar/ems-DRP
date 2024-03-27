from django import forms
from .models import Department, Role, Employee

class DepartmentForm(forms.ModelForm):
    class Meta: 
        model = Department
        fields = ('name', 'description', 'created_at')



class RoleForm(forms.ModelForm):
    class Meta: 
        model = Role
        fields = ('name', 'department')


class EmployeeForm(forms.ModelForm):
    class Meta: 
        model = Employee
        fields = ('name', 'email', 'role', 'phone_num', 'joined_date', 'address', 'department')