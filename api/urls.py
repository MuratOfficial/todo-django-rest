from django.urls import path
from api.views import TodoListView, TodoCreateListView, TodoUpdateDeleteListView, TodoCompletedView, signup

urlpatterns = [
    path('todos/complete/', TodoListView.as_view()),
    path('todos', TodoCreateListView.as_view()),
    path('todos/<int:pk>', TodoUpdateDeleteListView.as_view()),
    path('todos/<int:pk>/completed', TodoCompletedView.as_view()),
    path('signup', signup)

]
