from django.db import models

from .models import ville
from .models import produit

class pointdevente(models.Model):
    nom = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    adresse= models.CharField(max_length=200)
    tel= models.CharField(max_length=200)
    fax= models.CharField(max_length=200)
    ville= models.ForeignKey(ville, on_delete=models.CASCADE)
    idproduit = models.ForeignKey(produit, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table="pointdevente"