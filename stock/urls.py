from django.urls import path
from . import views

urlpatterns = [
    path('', views.insertinsert_stock, name='insert_stock'),
    path('show_stock/', views.show, name='show_stock'),
    path('graphe_stock/', views.show, name='graphe_stock'),
    path('bi_stock/', views.show, name='bi_stock'),
    path('edit_stock/<int:pk>', views.edit, name='edit_stock'),
    path('remove_stock/<int:pk>', views.remove, name='remove_stock'),
]



