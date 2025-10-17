from django.contrib import admin
from .models import Session


# --- Admin pour le modèle Session ---
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "topic",
        "confirence",
        "session_day",
        "start_time",
        "end_time",
        "room",
        "duration_minutes",
    )
    list_filter = ("confirence", "topic", "room", "session_day")
    search_fields = ("title", "topic", "room", "confirence__name")
    readonly_fields = ("created_at", "updated_at", "session_id")
    ordering = ("session_day", "start_time")

    fieldsets = (
        ("Informations principales", {
            "fields": ("title", "topic", "confirence", "room")
        }),
        ("Horaires de la session", {
            "fields": ("session_day", "start_time", "end_time")
        }),
        ("Dates d'enregistrement", {
            "fields": ("created_at", "updated_at")
        }),
    )

    def duration_minutes(self, obj):
        """Calcule la durée de la session en minutes."""
        if obj.start_time and obj.end_time:
            start = obj.start_time
            end = obj.end_time
            delta = (end.hour * 60 + end.minute) - (start.hour * 60 + start.minute)
            return delta
        return "RAS"

    duration_minutes.short_description = "Durée (minutes)"
