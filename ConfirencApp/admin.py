from django.contrib import admin
from .models import Confirence, Submission  

# Register your models here.
admin.site.site_header = "Gestion des Conférences"
admin.site.site_title = "Gestion des Conférences 25/26"
admin.site.index_title = "django app confirence"
admin.site.register(Confirence)
admin.site.register(Submission) 


