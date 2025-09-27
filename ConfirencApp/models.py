from django.db import models

# Create your models here.

class Confirence(models.Model):
    confirence_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    THEME = [
        ("ai", "computer science & ia"),
        ("se", "science & eng"),
        ("sc", "education"),
        ("it", "interdisciplinary themes"),
    ]

    theme = models.CharField(max_length=255, choices=THEME)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Submission(models.Model):
    submission_id = models.CharField(
        max_length=255,
        primary_key=True,
        unique=True
    )
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    keywords = models.TextField()
    paper = models.FileField(upload_to="papers/")

    STATUS = [
        ("submitted", "submitted"),
        ("under review", "under review"),
        ("accepted", "accepted"),
        ("rejected", "rejected"),
    ]

    status = models.CharField(max_length=50, choices=STATUS)
    submission_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        "UserApp.User",
        on_delete=models.CASCADE,
        related_name="submissions"
    )

    confirence = models.ForeignKey(
        "ConfirencApp.Confirence",
        on_delete=models.CASCADE,
        related_name="submissions"
    )

    def __str__(self):
        return self.title
