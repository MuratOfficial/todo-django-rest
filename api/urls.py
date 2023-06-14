from django.urls import path
from api.views import TodoListView

urlpatterns = [
    path('todos/complete/', TodoListView.as_view()),
]
