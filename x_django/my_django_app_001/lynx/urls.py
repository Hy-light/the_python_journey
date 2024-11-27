from django.urls import path

from . import views

urlpatterns = [
# connecting views and app urls
# We must link all urls here to the top level urls file of the my_django_app_001 dir
path('', views.home, name=""),

# Create a dynamic url to fetch the post description
path('article/<int:pk>/', views.singular_article, name="article")

    
]