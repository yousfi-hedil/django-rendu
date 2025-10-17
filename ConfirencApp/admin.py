from django.contrib import admin
from .models import Confirence, Submission


# =========================
# ADMIN POUR LES CONFÉRENCES
# =========================
@admin.register(Confirence)
class ConfirenceAdmin(admin.ModelAdmin):
    list_display = ('confirence_id', 'name', 'theme', 'location', 'start_date', 'end_date', 'created_at')
    list_filter = ('theme', 'location', 'start_date')
    search_fields = ('name', 'theme', 'location')
    readonly_fields = ('confirence_id', 'created_at', 'updated_at')  # ✅ champs existants
    ordering = ('-created_at',)


# =========================
# ADMIN POUR LES SOUMISSIONS
# =========================
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = (
        'submission_id', 'title', 'status', 'confirence', 'user', 'submission_date'
    )
    list_filter = ('status', 'confirence', 'submission_date')
    search_fields = ('title', 'keywords', 'user__username', 'confirence__name')
    readonly_fields = ('submission_id', 'submission_date', 'created_at', 'updated_at')
    ordering = ('-submission_date',)

    # Pour afficher des champs propres
    def get_confirence_name(self, obj):
        return obj.confirence.name
    get_confirence_name.short_description = 'Conférence'


