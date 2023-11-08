from habit.apps import HabitConfig
from django.urls import path

from habit.views import HabitCreateView, HabitDetailView, AllHabitListView, MyHabitListView, HabitUpdateView, \
    HabitDeleteView

app_name = HabitConfig.name

urlpatterns = [
    path('create-habit/', HabitCreateView.as_view()),
    path('get-habit/<int:pk>/', HabitDetailView.as_view()),
    path('all-habit/', AllHabitListView.as_view()),
    path('my-habit/', MyHabitListView.as_view()),
    path('update-habit/<int:pk>/', HabitUpdateView.as_view()),
    path('delete-habit/<int:pk>/', HabitDeleteView.as_view()),
]
