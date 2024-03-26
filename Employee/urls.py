
from django.contrib import admin
from django.urls import path
from .apiviews import EmployeeList, EmployeeDetail, EmployeeCreate, DepartmentList, DepartmentDetail, DepartmentCreate, RoleList, RoleDetail, RoleCreate
from .views import index


urlpatterns = [
    path('', index),
    # Employee paths
    path('employee/', EmployeeList.as_view(), name="EmployeeList"),
    path('employee/<int:pk>', EmployeeDetail.as_view(), name="EmployeeDetail"),
    path('employee/create', EmployeeCreate.as_view(), name="CreateEmployee"),

    # Department Paths
    path('department/', DepartmentList.as_view(), name="DepartmentList"),
    path('department/<int:pk>', DepartmentDetail.as_view(), name="DepartmentDetail"),
    path('department/create', DepartmentCreate.as_view(), name="CreateDepartment"),

    # Role Paths
    path('role/', RoleList.as_view(), name="RoleList"),
    path('role/<int:pk>', RoleDetail.as_view(), name="RoleDetail"),
    path('role/create', RoleCreate.as_view(), name="CreateRole"),
]
