from django import forms
from .models import Komentar

class KomentarForm(forms.ModelForm):
    class Meta:
        model = Komentar
        fields = ['isi', 'rating']
        widgets = {
            'isi': forms.Textarea(attrs={'rows': 3}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
