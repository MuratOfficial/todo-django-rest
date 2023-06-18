from django.utils import timezone
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.serializers import TodoListSerializer, TodoListUpdateSerializer
from todo.models import Todo
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.models import User

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request, None)
            user = User.objects.create_user(data['username'], password=data['password'])
            user.save()
            return JsonResponse({"token":"sometoken456"}, status=201)
        except IntegrityError:
            return JsonResponse({"error":"That username has already been taken. Please choose a new username"}, status=400)


class TodoListView(generics.ListAPIView):
    serializer_class = TodoListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)


class TodoCreateListView(generics.ListCreateAPIView):
    serializer_class = TodoListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TodoUpdateDeleteListView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    # def destroy(self, request, *args, **kwargs):

class TodoCompletedView(generics.UpdateAPIView):
    serializer_class = TodoListUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.datecompleted = timezone.now()
        serializer.save()
#



