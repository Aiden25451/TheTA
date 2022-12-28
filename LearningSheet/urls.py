from django.urls import path

from . import views

app_name = 'LearningSheet'
urlpatterns = [
    path('', views.index, name='index'),
]