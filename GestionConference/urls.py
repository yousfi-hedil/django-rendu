# GestionConference/urls.py (à mettre à jour)

from django.contrib import admin
from django.urls import path, include  # ⚠️ Assurez-vous d'importer 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    # AJOUTEZ CETTE LIGNE : 
    # Ceci mappe toutes les URLs de l'application 'ConfirencApp'
    # pour commencer par le préfixe 'conference/'.
    path('conference/', include('ConfirencApp.urls')), 
]