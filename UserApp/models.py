from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_id = models.CharField(
        max_length=8,
        primary_key=True,
        unique=True,
        editable=False
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    affiliation = models.CharField(max_length=255)

    ROLE = [
        ("participant", "Participant"),
        ("committee", "Organizing committee member"),
    ]
    role = models.CharField(
        max_length=255,
        choices=ROLE,
        default="participant"
    )

    nationality = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class OrganizingCommittee(models.Model):
    COMMITTEE_ROLES = [
        ("chair", "Chair"),
        ("co_chair", "Co-chair"),
        ("member", "Member"),
    ]
    committee_role = models.CharField(
        max_length=255,
        choices=COMMITTEE_ROLES
    )
    date_joined = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        "UserApp.User",
        on_delete=models.CASCADE,
        related_name="committees"
    )

    confirence = models.ForeignKey(
        "ConfirencApp.Confirence",
        on_delete=models.CASCADE,
        related_name="committees"
    )

    def __str__(self):
        return f"{self.committee_role} - {self.user}"
