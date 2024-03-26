
from django.contrib import admin
from django.urls import path
from .apiviews import EmployeeList, EmployeeDetail, EmployeeCreate

urlpatterns = [
    path('employee/', EmployeeList.as_view(), name="EmployeeList"),
    path('employee/<int:pk>', EmployeeDetail.as_view(), name="EmployeeDetail"),
    path('employe/create', EmployeeCreate.as_view(), name="CreateEmployee")
]
