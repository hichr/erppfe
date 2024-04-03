from django.db import models

from .models import ville


class produit(models.Model):
    nom = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    typeoroduit= models.CharField(max_length=200)
    proxachat= models.FloatField()
    prixvente= models.FloatField()
    taxproduit = models.FloatField()
    disponibilite = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table="produit"