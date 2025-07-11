from django.urls import path
from . import views

urlpatterns = [
    path('make_complete/<int:task_id>/', views.make_complete, name='make_complete'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
]
