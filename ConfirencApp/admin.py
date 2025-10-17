from django.contrib import admin
from .models import Confirence, Submission


# --- Personnalisation du panneau d'administration ---
admin.site.site_header = "Gestion des Conférences"
admin.site.site_title = "Gestion des Conférences 25/26"
admin.site.index_title = "Application Django - Confirence"


# --- Inline : permet d'ajouter des Submissions depuis la page d'une Confirence ---
class SubmissionInline(admin.StackedInline):
    model = Submission
    extra = 1
    readonly_fields = ("submission_date", "submission_id", "created_at", "updated_at")


# --- Admin du modèle Confirence ---
@admin.register(Confirence)
class AdminConfirenceModel(admin.ModelAdmin):
    list_display = ("name", "theme", "start_date", "end_date", "duration_days")
    ordering = ("start_date",)
    list_filter = ("theme", "location")
    search_fields = ("name", "description", "theme", "location")
    date_hierarchy = "start_date"

    fieldsets = (
        ("Informations Générales", {
            "fields": ("name", "theme", "description")
        }),
        ("Détails logistiques", {
            "fields": ("location", "start_date", "end_date")
        }),
        ("Dates d'enregistrement", {
            "fields": ("created_at", "updated_at")
        }),
    )

    readonly_fields = ("created_at", "updated_at")
    inlines = [SubmissionInline]

    def duration_days(self, obj):
        """Calcule la durée de la conférence en jours."""
        if obj.start_date and obj.end_date:
            return (obj.end_date - obj.start_date).days
        return "RAS"

    duration_days.short_description = "Durée (jours)"
    
    
    
    
    
    
@admin.action(description="Marquer les inscriptions sélectionnées comme payées")
def mark_as_payed(modeladmin,req,queryset):
    queryset.update(payed=True)
@admin.action(description="Marquer les soumissions sélectionnées comme acceptées")  
def mark_as_accepted(modeladmin,req,queryset):
    queryset.update(status='accepted')
    
    
    
    
    
# --- Admin du modèle Submission ---
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = (
        "submission_id",
        "title",
        "confirence",
        "user",
        "status",
        "submission_date",
    )
    list_filter = ("status", "confirence", "submission_date")
    search_fields = ("title", "keywords", "user__username")
    readonly_fields = (
        "submission_id",
        "submission_date",
        "created_at",
        "updated_at",
    )
    ordering = ("-submission_date",)
    
    actions =[mark_as_payed,mark_as_accepted]
    fieldsets = (
        ("Informations sur la soumission", {
            "fields": ("title", "abstract", "keywords", "file_upload", "confirence", "user", "status")
        }),
        ("Dates", {
            "fields": ("submission_date", "created_at", "updated_at")
        }),
    )
    
 

