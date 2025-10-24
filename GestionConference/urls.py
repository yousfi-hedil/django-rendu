# GestionConference/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conference/', include('ConfirencApp.urls')),
    path('', RedirectView.as_view(url='/conference/liste/')),  # Redirige la racine vers la liste des conférences
    path('users/', include('UserApp.urls')),  # URLs de l'application UserApp
]