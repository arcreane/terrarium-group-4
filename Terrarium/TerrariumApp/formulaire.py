from django.forms import ModelForm              #Importation du modele form de django
from .models import terrarium                   #Importation de la classe terrarium

class terrariumform(ModelForm):                 #Création de la classe du formulaire
    class Meta:                                 #Classe qui utilise une classe et non un objet
        model = terrarium                       #Analyse du modele terrarium pour créer le même
        fields = ['nom','temperature','taille','humidite'] #Champs qui vont être accessible sur le formulaire