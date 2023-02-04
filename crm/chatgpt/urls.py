from django.urls import path
from . import views

urlpatterns = [
    path('', views.GptView.as_view(),name='GptView'),
    # Post 
]