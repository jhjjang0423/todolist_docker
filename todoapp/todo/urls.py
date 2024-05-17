from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:id>/', views.edit_todo, name='edit_todo'),
    path('delete/<int:id>/', views.delete_todo, name='delete_todo'),
]
