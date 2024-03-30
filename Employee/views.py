from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Department, Role

# from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.decorators import api_view

def index(request):
    return HttpResponse("<h1>Employee Management System</h1>")

