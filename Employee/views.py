from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Department, Role
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

def index(request):
    return HttpResponse("<h1>Employee Management System</h1>")

class EmployeeList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'employee_list.html'

    def get(self, request):
        queryset = Employee.objects.all()
        return HttpResponse({'employees': queryset})