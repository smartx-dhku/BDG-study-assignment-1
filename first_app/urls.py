from django.urls import path
from . import views

urlpatterns = [
    path('<name>/<age>/', views.index),
    path('', views.advance),
]