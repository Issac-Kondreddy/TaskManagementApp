from rest_framework import serializers
from .models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Tasks
        fields = ['task_id', 'task_name', 'task_description', 'task_status', 'created_at', 'updated_at', 'user']


    def validate_task_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Task name should be at least 5 characters long.")
        return value

    def validate_task_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Task description should be at least 10 characters long.")
        return value
    
    def validate_task_status(self, value):
        valid_status = ['Pending', 'In Progress', 'Completed']
        if value not in valid_status:
            raise serializers.ValidationError(f"Task status must be one of: {', '.join(valid_status)}.")
        return value

