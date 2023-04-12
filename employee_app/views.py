from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Employee
# Create your views here.

class EmployeeHome(ListView):
    model = Employee
    template_name = 'employee_app/employee_home.html'
    
    