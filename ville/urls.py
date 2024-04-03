from django.urls import path
from . import views

urlpatterns = [
    path('', views.insert, name='insert-emp'),
    path('show/', views.show, name='show-emp'),
    path('edit/<int:pk>', views.edit, name='edit-emp'),
    path('remove/<int:pk>', views.remove, name='remove-emp'),
]



