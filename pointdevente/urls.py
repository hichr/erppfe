from django.urls import path
from . import views

urlpatterns = [
    path('', views.insertinsert_pointdevente, name='insert_pointdevente'),
    path('show_pointdevente/', views.show, name='show_pointdevente'),
    path('graphe_pointdevente/', views.show, name='graphe_pointdevente'),
    path('bi_pointdevente/', views.show, name='bi_pointdevente'),
    path('edit_pointdevente/<int:pk>', views.edit, name='edit_pointdevente'),
    path('remove_pointdevente/<int:pk>', views.remove, name='remove_pointdevente'),
]



