from django.db import models

from .models import produit
from .models import ville


class stock(models.Model):
    nom = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    typestock= models.CharField(max_length=200)
    qteentree= models.CharField(max_length=200)
    qtesortie= models.CharField(max_length=200)
    codeproduit = models.ForeignKey(produit, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table="stock"