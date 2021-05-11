from django.contrib import admin

# Importantion des modèles pour les avoir dans admin

from .models import terrarium, terrariumAdmin
admin.site.register(terrarium, terrariumAdmin)
