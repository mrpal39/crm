from django.urls import path
from . import views

urlpatterns = [
    path('', views.qoutes, name='qoutes'),
    # Post 
]