from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'user'
        if commit:
            user.save()
        return user

class MitraRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'no_hp', 'nik', 'foto_ktp', 'selfie_ktp', 'tanggal_lahir', 'password1', 'password2']
        widgets = {
            'tanggal_lahir': forms.DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'mitra'
        user.no_hp = self.cleaned_data.get('no_hp')
        user.nik = self.cleaned_data.get('nik')
        user.foto_ktp = self.cleaned_data.get('foto_ktp')
        user.selfie_ktp = self.cleaned_data.get('selfie_ktp')
        user.tanggal_lahir = self.cleaned_data.get('tanggal_lahir')
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    pass
