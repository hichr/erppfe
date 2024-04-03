from django.urls import path
from . import views

urlpatterns = [
    path('', views.insertinsert_categorieproduit, name='insert_categorieproduit'),
    path('show_categorieproduit/', views.show, name='show_categorieproduit'),
    path('graphe_categorieproduit/', views.show, name='graphe_categorieproduit'),
    path('bi_categorieproduit/', views.show, name='bi_categorieproduit'),
    path('edit_categorieproduit/<int:pk>', views.edit, name='edit_categorieproduit'),
    path('remove_categorieproduit/<int:pk>', views.remove, name='remove_categorieproduit'),
]



