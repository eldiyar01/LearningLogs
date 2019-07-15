from django.urls import path

from .views import home, topics, topic, create_topic, edit_topic, delete_topic, \
    create_entry, edit_entry, delete_entry

app_name = 'learning_logs'
urlpatterns = [
    path('', home, name='home'),
    path('topics/', topics, name='topics'),
    path('topic/<int:pk>/', topic, name='topic'),
    path('topic/create/', create_topic, name='create_topic'),
    path('topic/<int:pk>/edit/', edit_topic, name='edit_topic'),
    path('topic/<int:pk>/delete', delete_topic, name='delete_topic'),
    path('topic/<int:pk>/entry/create/', create_entry, name='create_entry'),
    path('entry/<int:pk>/edit/', edit_entry, name='edit_entry'),
    path('entry/<int:pk>/delete', delete_entry, name='delete_entry'),
]