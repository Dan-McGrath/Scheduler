from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Shift, Schedule

class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()
    
    # formats a day as a td
    # filters shift by day
    def formatday(self, day, shifts):
        shifts_per_day = shifts.filter(start_time__day=day)
        d = ''
        for shift in shifts_per_day:
            d += f'<li>{shift.get_html_url} shift</li>'
        
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'
        
    # formats a week as a tr
    def formatweek(self, theweek, shifts):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, shifts)
        return f'<tr> {week} </tr>'

    # format a month as a table
    # filter shifts by year and month
    def formatmonth(self, withyear=True):
        shifts = Shift.objects.filter(start_time__year=self.year, start_time__month=self.month)
        calendar = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        calendar += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        calendar += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            calendar += f'{self.formatweek(week, shifts)}\n'
        return calendar