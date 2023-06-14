from todo.models import Todo
from rest_framework import serializers

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created', 'datecompleted', 'important', 'user']
