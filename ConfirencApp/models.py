from django.db import models
from django.core.validators import MaxLengthValidator
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinLengthValidator , FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from datetime import date
import random 
import string 
# Create your models here.

def validate_max_keywords(value):
    """
    Vérifie que la chaîne de mots-clés (séparés par des virgules)
    ne contient pas plus de 10 mots-clés.
    """
    # La ligne 'keywords_list = [k.strip() ...' doit être indentée ici
    keywords_list = [k.strip() for k in value.split(',') if k.strip()]
    max_keywords = 10
    if len(keywords_list) > max_keywords:
        # La levée de l'exception doit également être indentée
        raise ValidationError(
            _('Le nombre maximal de mots-clés est de %(max_keywords)s. Vous en avez fourni %(current_count)s.'),
            params={'max_keywords': max_keywords, 'current_count': len(keywords_list)},
            code='max_keywords_exceeded'
        )
        
        
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
    description = models.CharField(max_length=255,
                                   validators=[
        MaxLengthValidator(30,"vous avez depasser le nombre de caractere autoriser")
    ])
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def clean(self):
        # Validation : start_date doit être <= end_date
        if self.start_date > self.end_date:
            raise ValidationError("La date de début de la conférence doit être inférieure ou égale à la date de fin.")
        super().clean()
    
    def __str__(self):
        return self.name

   
class Submission(models.Model):
    submission_id = models.CharField(
        max_length=255,
        primary_key=True,
        unique=True,
        blank=True,
        editable=False 
    )
    title = models.CharField(max_length=255,validators=[
            RegexValidator(
                regex=r'^[A-Za-zÀ-ÿ\s]+$',
                message='Le titre doit contenir uniquement des lettres et des espaces.'
            )
        ])
    abstract = models.TextField()
    keywords = models.TextField(validators=[validate_max_keywords])
    paper = models.FileField(upload_to="papers/",validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

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
    
    
    def generate_unique_id(self):
        
        prefix = "SUB"
        length = 8
        characters = string.ascii_uppercase + string.digits
        
        while True:
            # Génère 8 caractères aléatoires
            random_part = ''.join(random.choice(characters) for _ in range(length))
            new_id = f"{prefix}{random_part}"
            # Vérifie si cet ID existe déjà
            if not Submission.objects.filter(submission_id=new_id).exists():
                return new_id
            
            
            
    def clean(self):
       
        today = date.today()
       
        confirence_instance = getattr(self, 'confirence', None)
        if confirence_instance is not None:
            
            if confirence_instance.start_date < today:
                raise ValidationError(
                    {'confirence': _('La soumission ne peut être faite que pour des conférences dont la date de début est future.')}
                )

        max_submissions_per_day = 3
        
        
        if self.user_id is not None:
            
            
            submissions_today = Submission.objects.filter(
                user=self.user,
                
                submission_date=today 
            ).exclude(pk=self.pk).count()
            
            if submissions_today >= max_submissions_per_day:
                
                raise ValidationError(
                    {'user': _('Vous avez atteint la limite de %(limit)s soumissions par jour.') % {'limit': max_submissions_per_day}}
                )

        
        super().clean()
    def save(self, *args, **kwargs):
        # Si c'est un nouvel enregistrement (l'ID n'est pas encore défini)
        if not self.submission_id:
            self.submission_id = self.generate_unique_id()
        
        # Appeler la méthode save originale
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title


