from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, OrganizingCommittee


# --- Admin pour User ---
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "user_id",
        "username",
        "first_name",
        "last_name",
        "email",
        "role",
        "affiliation",
        "nationality",
        "date_joined",
    )
    list_filter = ("role", "affiliation", "nationality", "is_staff", "is_superuser")
    search_fields = ("user_id", "username", "first_name", "last_name", "email")
    readonly_fields = ("user_id", "created_at", "updated_at", "date_joined", "last_login")
    ordering = ("username",)

    fieldsets = (
        ("Informations personnelles", {
            "fields": ("username", "first_name", "last_name", "email", "affiliation", "nationality")
        }),
        ("Rôle & permissions", {
            "fields": ("role", "is_staff", "is_superuser", "is_active", "groups", "user_permissions")
        }),
        ("Dates", {
            "fields": ("created_at", "updated_at", "date_joined", "last_login")
        }),
        ("Mot de passe", {
            "fields": ("password",)
        }),
    )


# --- Admin pour OrganizingCommittee ---
@admin.register(OrganizingCommittee)
class OrganizingCommitteeAdmin(admin.ModelAdmin):
    list_display = (
        "committee_role",
        "user",
        "confirence",
        "date_joined",
    )
    list_filter = ("committee_role", "confirence")
    search_fields = ("user__username", "user__first_name", "user__last_name", "confirence__name")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("date_joined",)

    fieldsets = (
        ("Informations du comité", {
            "fields": ("user", "confirence", "committee_role", "date_joined")
        }),
        ("Dates", {
            "fields": ("created_at", "updated_at")
        }),
    )
