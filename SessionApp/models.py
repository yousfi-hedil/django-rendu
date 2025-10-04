from django.db import models
from django.core.exceptions import ValidationError 
from ConfirencApp.models import Confirence
from django.core.validators import RegexValidator
# Create your models here.


class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    session_day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=255,
                            validators=[
        RegexValidator(
            regex=r'^[A-Za-z0-9]+$',
            message="Le nom de la salle ne doit contenir que des lettres et des chiffres (pas de caractères spéciaux ou d'espaces)."
        )
    ]
)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    confirence = models.ForeignKey(
        Confirence,
        on_delete=models.CASCADE,
        related_name="sessions"
    )

    
    def clean(self):
        super().clean()
        # Vérifier si confirence est défini via confirence_id (clé étrangère)
        if self.confirence_id is not None:
            start_date = self.confirence.start_date
            end_date = self.confirence.end_date
            if start_date and end_date:
                if self.session_day < start_date or self.session_day > end_date:
                    raise ValidationError({
                        'session_day': f"La date de la session ({self.session_day}) doit être comprise entre la date de début ({start_date}) et la date de fin ({end_date}) de la conférence."
                    })
            else:
                raise ValidationError({
                    'session_day': "La conférence associée doit avoir des dates de début et de fin définies."
                })
        if self.start_time and self.end_time:
            if self.end_time <= self.start_time:
                raise ValidationError({
                'end_time': "L'heure de fin doit être strictement supérieure à l'heure de début."
            })
    def save(self, *args, **kwargs):
        """
        Surcharge de save() pour forcer la validation complète avant sauvegarde.
        """
        self.full_clean()  
        super().save(*args, **kwargs)
        
        def __str__(self):
            return f"{self.title} - {self.session_day}"
