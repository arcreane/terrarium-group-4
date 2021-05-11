from django.db import models
from django.contrib import admin
#Création de la classe modèle

class terrarium(models.Model):
    nom = models.CharField(max_length=55)
    temperature = models.DecimalField(max_digits=30, decimal_places=1)
    taille = models.IntegerField(max_length=None)
    humidite = models.DecimalField(max_digits=30, decimal_places=1)

#Création du modèle pour faire les incrémentations
class terrariumAdmin(admin.ModelAdmin):
     list_display = ('nom','temperature','taille','humidite')
     list_filter = ('nom',)
     search_fields = ['nom','temperature','taille','humidite']

