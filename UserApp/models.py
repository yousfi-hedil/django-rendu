from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator   
def genreate_user_id():
    return "USER"+uuid.uuid4().hex[:4].upper()

def verify_email(email):
    domaines=["esprit.tn","seasame.com","gmail.com","yahoo.com","hotmail.com"]
    email_domain=email.split('@')[-1]
    if email_domain not in domaines:
        raise ValidationError(f"Email domain invalid ")
    
name_validators = RegexValidator(
    regex= r'^[a-zA-Z\s-]+$',
        message="Name must contain only letters, spaces, and hyphens."
     
     )


class User(AbstractUser):
    user_id = models.CharField(
        max_length=8,
        primary_key=True,
        unique=True,
        editable=False
    )
    first_name = models.CharField(max_length=255,validators=[name_validators])
    last_name = models.CharField(max_length=255,validators=[name_validators])
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
    email = models.EmailField(unique=True,validators=[verify_email])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self,*args,**kwargs):
        if not self.user_id:
            newid=genreate_user_id()
            while User.objects.filter(user_id=newid).exists():
                newid= genreate_user_id()
            self.user_id=newid
        super().save(*args,**kwargs)
        

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
    
    
    
    
