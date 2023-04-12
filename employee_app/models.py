from django.db import models

from django.urls import reverse
from django.core.validators import RegexValidator
# Create your models here.

#Employee Model

class Employee(models.Model):
#     SUNDAY = 'SU'
#     MONDAY = 'MO'
#     TUESDAY = 'TU'
#     WEDNESDAY = 'WE'
#     THURSDAY = 'TH'
#     FRIDAY = 'FR'
#     SATURDAY = 'SA'
#     DAYS_OF_WEEK = [
#         (SUNDAY, 'Sunday'),
#         (MONDAY, 'Monday'),
#         (TUESDAY, 'Tuesday'),
#         (WEDNESDAY, 'Wednesday'),
#         (THURSDAY, 'Thursday'),
#         (FRIDAY, 'Friday'),
#         (SATURDAY, 'Sunday')
#     ]

    MORNING = 'MO'
    AFTERNOON = 'AF'
    MID = 'MI'
    NIGHT_AUDIT = 'NA'
    PREFERED_SHIFT_CHOICES = [
        (MORNING, 'Morning'),
        (MID, 'Mid/Split'),
        (AFTERNOON, 'Afternoon'),
        (NIGHT_AUDIT, 'Night Audit')
    ]


    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    phone_regex = RegexValidator(regex=r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, unique=True) # Validators should be a list
    paid_time_off = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    sick_days = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    hours_worked = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    prefered_shift = models.CharField(
        max_length=2,
        choices=PREFERED_SHIFT_CHOICES,
        default=MORNING,
        null=True,
    )

    #hourly_pay = models.DecimalField(max_digits=6, decimal_places=2)
    #hire_date = models.DateField(editable=False, blank=True)

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})

