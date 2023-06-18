from todo.models import Todo
from rest_framework import serializers

class TodoListSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()
    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created', 'datecompleted', 'important']

class TodoListUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        read_only_fields = ['title', 'memo', 'created', 'datecompleted', 'important']
        fields = ['id']


