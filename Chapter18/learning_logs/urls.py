"""Defines URL patterns for learning_logs."""

from django.conf.urls import url

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    #url(r'^$', views.index, name='index'),
    url('', views.index, name='index'),
    # Page that shows all topics.
    url('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    url('topics/<int:topic_id>/', views.topic, name='topic'),

]
