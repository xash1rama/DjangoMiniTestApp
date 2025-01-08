from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'is_completed']

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Поле title не может быть пустым.")
        return value
