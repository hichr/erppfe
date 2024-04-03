from django.urls import path
from . import views

urlpatterns = [
    path('', views.insertinsert_client, name='insert_client'),
    path('show_client/', views.show, name='show_client'),
    path('graphe_client/', views.show, name='graphe_client'),
    path('bi_client/', views.show, name='bi_client'),
    path('edit_client/<int:pk>', views.edit, name='edit_client'),
    path('remove_client/<int:pk>', views.remove, name='remove_client'),
]



