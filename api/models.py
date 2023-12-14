from django.db import models

class Concessionnaire(models.Model):
    nom = models.CharField(max_length=255)
    numero_siret = models.PositiveIntegerField()
    code_postal = models.CharField(max_length=5)

class Voiture(models.Model):
    marque = models.CharField(max_length=255)
    modele = models.CharField(max_length=255)
    chevaux = models.PositiveIntegerField()
    concessionnaire = models.ForeignKey(Concessionnaire, on_delete=models.CASCADE)
