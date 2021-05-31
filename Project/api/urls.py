from django.urls import path

from api.views import ()
from rest_framework import permissions


urlpatterns = [
    path('timetable/', TimeTableView.as_view(), name='timetable'),
]
