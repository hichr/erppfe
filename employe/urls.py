from django.urls import path
from . import views

urlpatterns = [
    path('', views.insertinsert_employe, name='insert_employe'),
    path('show_employe/', views.show, name='show_employe'),
    path('graphe_employe/', views.show, name='graphe_employe'),
    path('bi_employe/', views.show, name='bi_employe'),
    path('edit_employe/<int:pk>', views.edit, name='edit_employe'),
    path('remove_employe/<int:pk>', views.remove, name='remove_employe'),
]



