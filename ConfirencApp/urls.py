from django.urls import path
from . import views

urlpatterns = [
    path("creer/", views.ConfirenceCreate.as_view(), name='creer_confirence'), # 👈 AJOUTEZ CECI
    # URLs de liste
    path("liste/", views.liste_confirences, name="liste_confirences"),          # Vue fonctionnelle
    #path("listview/", views.ConfirenceList.as_view(), name="listview_confirences"), # Vue générique (Class-Based View)
    path("details/<int:pk>/", views.ConfirenceDetails.as_view(), name="details_confirence"),
    # Si l'utilisateur tape juste 'details/' sans PK, rediriger vers la liste
    path("details/", views.details_index, name="details_index"),
    # Route pour ajouter une conférence (utilisée par les templates)
    path("ajouter/", views.ConfirenceCreate.as_view(), name="ajouter_confirence"),
    # Alias pour compatibilité : permet d'ouvrir le même formulaire via /conference/form/
    path("form/", views.ConfirenceCreate.as_view(), name="form_confirence"),
    path('modifier/<int:pk>/', views.ConfirenceUpdate.as_view(), name='modifier_confirence'),
    # Path de suppression
    path('supprimer/<int:pk>/', views.ConfirenceDelete.as_view(), name='supprimer_confirence'),
]