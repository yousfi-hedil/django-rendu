from django.shortcuts import render
from .models import Conference  # Assure-toi que ton modèle s'appelle bien "Conference"

# Create your views here.
def liste_conferences(request):
    # Logique pour récupérer la liste des conférences depuis la base de données
    conferences_liste = Conference.objects.all()
    
    # Retourne la page HTML avec la liste
    return render(request, 'confirence/liste.html', {'liste': conferences_liste})
class confirenceList(ListView):
    model = Confirence
    template_name = 'confirence/liste.html'
    context_object_name = 'liste'   