from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def home(request):
    return render(request, 'tasks.html')