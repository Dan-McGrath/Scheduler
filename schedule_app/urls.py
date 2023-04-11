from django.urls import path
from . import views

urlpatterns = [
    path('', views.ScheduleHome.as_view(), name='schedule-home'),
    path('schedule/', views.ScheduleList.as_view(), name = 'schedule-list'),
    path('schedule/create/', views.ScheduleCreate.as_view(), name = 'schedule-create'),
    path('schedule/update/<str:pk>', views.ScheduleUpdate.as_view(), name = 'schedule-update'),
    path('schedule/delete/<str:pk>', views.ScheduleDelete.as_view(), name = 'schedule-delete'),
    
]

