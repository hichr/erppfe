from django.urls import path
from . import views

urlpatterns = [
    path('', views.insertinsert_produit, name='insert_produit'),
    path('show_produit/', views.show, name='show_produit'),
    path('graphe_produit/', views.show, name='graphe_produit'),
    path('bi_produit/', views.show, name='bi_produit'),
    path('edit_produit/<int:pk>', views.edit, name='edit_produit'),
    path('remove_produit/<int:pk>', views.remove, name='remove_produit'),
]



