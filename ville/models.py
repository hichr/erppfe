from django.db import models


class ville(models.Model):
    nom = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table="ville"