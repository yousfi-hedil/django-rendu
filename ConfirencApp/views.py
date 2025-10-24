from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Confirence  # ⚠️ Ton modèle s'appelle "Confirence", pas "Conference"
from .forms import ConferenceForm   

# --- Vue fonctionnelle : liste des conférences ---
def liste_confirences(request):
    """Affiche la liste des conférences (vue fonctionnelle)."""
    confirences_liste = Confirence.objects.all()
    # Le dossier Templates du projet contient liste.html à la racine
    return render(request, "liste.html", {"liste": confirences_liste})


# --- Vue générique : liste des conférences ---
class ConfirenceList(ListView):
    model = Confirence
    context_object_name = "liste"
    # utilise le template global liste.html
    template_name = "liste.html"


# --- Vue générique : détails d'une conférence ---
class ConfirenceDetails(DetailView):
    model = Confirence
    context_object_name = "confirence"
    # le template details.html se trouve dans le dossier Templates du projet
    template_name = "details.html"


# --- Vue générique : création d'une conférence ---
class ConfirenceCreate(CreateView):
    model = Confirence
    # utilise le template form.html présent dans le dossier Templates
    template_name = "form.html"
    # fields = "__all__"
    form_class = ConferenceForm  # Utilisation du formulaire personnalisé
    success_url = reverse_lazy("liste_confirences")
# --- Vue générique : suppression d'une conférence (DeleteView) ---
class ConfirenceDelete(DeleteView):
    model = Confirence
    # Django utilise par défaut un template nommé 'confirence_confirm_delete.html'
    # mais il est souvent plus simple de spécifier le nom :
    template_name = "confirence_confirm_delete.html"
    # Redirige après la suppression :
    success_url = reverse_lazy("liste_confirences")
class ConfirenceUpdate(UpdateView):
    model = Confirence
    # On réutilise souvent le même template de formulaire que pour la création
    template_name = "form.html"
    # fields = "__all__"
    form_class = ConferenceForm  # Utilisation du formulaire personnalisé
    # Redirige vers les détails de la conférence modifiée (vous pouvez aussi utiliser 'liste_confirences')
    # Attention, si vous utilisez 'details_confirence', il faudra que l'URL soit nommée ainsi
    # Ici, je mets 'liste_confirences' pour simplifier :
    success_url = reverse_lazy("liste_confirences")


def details_index(request):
    """Redirige 'details/' sans PK vers la page de liste pour éviter une 404 peu utile."""
    return redirect('liste_confirences')