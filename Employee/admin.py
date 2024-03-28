from django.contrib import admin

import Employee.models as models


class DepartmentAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description', 'created_at')
    list_filter = ('created_at', 'id', 'name', 'description')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


class RoleAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'department')
    list_filter = ('department', 'id', 'name')
    search_fields = ('name',)


class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'email',
        'role',
        'phone_num',
        'joined_date',
        'address',
        'department',
    )
    list_filter = (
        'role',
        'joined_date',
        'department',
        'id',
        'name',
        'email',
        'phone_num',
        'address',
    )
    search_fields = ('name',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Department, DepartmentAdmin)
_register(models.Role, RoleAdmin)
_register(models.Employee, EmployeeAdmin)
