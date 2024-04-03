from django.db import models

from .models import ville


class client(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    adresse= models.CharField(max_length=200)
    tel= models.CharField(max_length=200)
    fax= models.CharField(max_length=200)
    ville= models.ForeignKey(ville, on_delete=models.CASCADE)
    email= models.CharField(max_length=200)
    motdepasse= models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table="client"