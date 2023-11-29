from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('task/',views.task, name='task'),
    path('task/', views.elapsed_time_view, name='task'), 
]