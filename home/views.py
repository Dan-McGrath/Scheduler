from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from datetime import datetime
from employee_app.models import Employee
from schedule_app.models import Shift
from schedule_app.utils import Calendar

# Create your views here.

class HomeView(ListView):
    model = Shift
    template_name = 'home/base.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # get todays date
        todays_date = get_date(self.request.GET.get('day', None))

        # Make Calendar with todays date
        calendar = Calendar(todays_date.year, todays_date.month)

        # turn calendar into table
        html_calendar = calendar.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_calendar)

        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()