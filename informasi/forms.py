# informasi/forms.py

from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nama Lengkap Anda'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email@anda.com'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subjek Pesan'}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Tulis pesan Anda di sini...'}),
        }
