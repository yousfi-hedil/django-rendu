from django import forms
from .models import Confirence


class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Confirence
        fields = ['name', 'theme', 'start_date', 'end_date', 'location', 'description']
        labels = {
            'name': 'Nom de la conférence', 
            'theme': 'Thème',
            'start_date': 'Date de début',
            'end_date': 'Date de fin',
            'location': 'Lieu',
            'description': 'Description',
        }
        
        widgets = { 
                   
            'name': forms.TextInput(attrs={'placeholder': 'Nom de la conférence'}),
            'theme': forms.TextInput(attrs={'placeholder': 'Thème de la conférence'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),

            
        }
        help_texts = {
            'name': 'Entrez le nom complet de la conférence.',
            'theme': 'Indiquez le thème principal de la conférence.',
            'start_date': 'Sélectionnez la date de début de la conférence.',
            'end_date': 'Sélectionnez la date de fin de la conférence.',
            'location': 'Indiquez le lieu où se tiendra la conférence.',
            'description': 'Fournissez une brève description de la conférence.',
        }
        error_messages = {
            'name': {
                'max_length': 'Le nom de la conférence est trop long.',
                'required': 'Le nom de la conférence est obligatoire.',
            },
            'theme': {
                'max_length': 'Le thème est trop long.',
                'required': 'Le thème de la conférence est obligatoire.',
            },
            'start_date': {
                'invalid': 'Entrez une date de début valide.',
                'required': 'La date de début est obligatoire.',
            },
            'end_date': {
                'invalid': 'Entrez une date de fin valide.',
                'required': 'La date de fin est obligatoire.',
            },
        }
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError("La date de fin doit être postérieure à la date de début.")
        return cleaned_data
    