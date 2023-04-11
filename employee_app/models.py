from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
# Create your models here.

#Employee Model

class Employee(models.Model):
    SUNDAY = 'SU'
    MONDAY = 'MO'
    TUESDAY = 'TU'
    WEDNESDAY = 'WE'
    THURSDAY = 'TH'
    FRIDAY = 'FR'
    SATURDAY = 'SA'
    DAYS_OF_WEEK = [
        (SUNDAY, 'Sunday'),
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Sunday')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    phone_regex = RegexValidator(regex=r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, unique=True) # Validators should be a list
    hire_date = models.DateField()
    pto = models.IntegerField(default=0)
    sick_days = models.IntegerField(default=0)
    hourly_pay = models.DecimalField(max_digits=6, decimal_places=2)
    

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})

