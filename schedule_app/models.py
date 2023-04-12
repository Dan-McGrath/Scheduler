from django.db import models
from django.urls import reverse
from employee_app.models import Employee
# Create your models here.

class Shift(models.Model):
    MORNING = 'MO'
    AFTERNOON = 'AF'
    MID = 'MI'
    NIGHT_AUDIT = 'NA'
    SHIFT_CHOICES = [
        (MORNING, 'Morning'),
        (MID, 'Mid/Split'),
        (AFTERNOON, 'Afternoon'),
        (NIGHT_AUDIT, 'Night Audit')
    ]
    shift_name = models.CharField(
        max_length=2,
        choices=SHIFT_CHOICES,
        default=MORNING,
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    @property
    def get_html_url(self):
        url = reverse('home:shift-detail', args=(self.id,))
        return f'<a href="{url}"> {self.shift_name} </a>'

    class Meta:
        verbose_name = ("Shift")
        verbose_name_plural = ("Shifts")

    def __str__(self):
        return f'{self.shift_name} shift'

    def get_absolute_url(self):
        return reverse("Shift_detail", kwargs={"pk": self.pk})

class Day(models.Model):
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
        (SATURDAY, 'Sunday'),
    ]
    

    class Meta:
        verbose_name = ("Day")
        verbose_name_plural = ("Days")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Day_detail", kwargs={"pk": self.pk})


class Schedule(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    

    class Meta:
        verbose_name = ("Schedule")
        verbose_name_plural = ("Schedules")

    def __str__(self):
        return f'{self.start_date}-{self.end_date}'

    def get_absolute_url(self):
        return reverse("Schedule-detail", kwargs={"pk": self.pk})



