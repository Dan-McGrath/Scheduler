from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Shift

# Create your views here.
class ScheduleHome(ListView):
    model = Shift
    template_name = 'schedule_app/schedule_home.html'
    