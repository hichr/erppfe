from django.db import models

from .models import produit


class categorie_produit(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    codeproduit = models.ForeignKey(produit, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table="categorie_produit"