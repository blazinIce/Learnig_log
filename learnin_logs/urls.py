"""Defines URL pattern for learnin_logs"""

from django.urls import path

from . import views

app_name = 'learnin_logs'
urlpatterns = [
    #homepage
    path('', views.index, name='index'),
    # page that shows all topics
    path('topics/', views.topics, name='topics'),
    #detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]