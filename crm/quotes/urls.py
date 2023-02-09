from django.urls import path
from . import views
app_name="qoutes"
urlpatterns = [
    path('', views.qoutes, name='scraper'),
    # Post 
]