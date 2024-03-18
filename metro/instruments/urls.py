from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('instruments/', views.instruments),
    path('about/', views.about),
]
