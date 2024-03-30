from rest_framework import serializers
from .models import Department, Role, Employee

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = [
            'name',
            'description',
            'created_at'
        ]

class RoleSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Role
        fields = [
            'name',
            'department'
        ]

class EmployeeSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()
    department = serializers.StringRelatedField()
    class Meta:
        model = Employee
        fields = [
            'name',
            'email',
            'role',
            'phone_num',
            'joined_date',
            'address',
            'department'
        ]