from django.urls import path
from .views import TaskListCreateView
from .views import home


urlpatterns = [
    path('', home, name='home'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create')
]
