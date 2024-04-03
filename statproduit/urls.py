from django.urls import path
from . import views

urlpatterns = [
    path('', views.insertinsert_statproduit, name='insert_statproduit'),
    path('show_statproduit/', views.show, name='show_statproduit'),
    path('graphe_statproduit/', views.show, name='graphe_statproduit'),
    path('bi_statproduit/', views.show, name='bi_statproduit'),
    path('edit_statproduit/<int:pk>', views.edit, name='edit_statproduit'),
    path('remove_statproduit/<int:pk>', views.remove, name='remove_statproduit'),
]



