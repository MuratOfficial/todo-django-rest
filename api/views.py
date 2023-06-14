from rest_framework import generics
from api.serializers import TodoListSerializer

class TodoListView(generics.ListAPIView):
    serializer_class = TodoListSerializer

