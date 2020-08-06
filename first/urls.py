from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.students, name='students'),
    path('scores', views.scores, name='scores')
]