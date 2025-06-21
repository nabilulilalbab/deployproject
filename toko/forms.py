from django import forms
from .models import Toko, Produk,KomentarToko

class TokoForm(forms.ModelForm):
    class Meta:
        model = Toko
        fields = ['nama', 'alamat', 'kabupaten', 'latitude', 'longitude']
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }


class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama', 'deskripsi', 'harga','foto_produk', 'is_active']


class KomentarTokoForm(forms.ModelForm):
    class Meta:
        model = KomentarToko
        fields = ['isi', 'rating']
        widgets = {
            'isi': forms.Textarea(attrs={
                'rows': 3, 'placeholder': 'Tulis komentar Anda...', 
                'class': 'w-full p-2 border rounded'
            }),
            'rating': forms.NumberInput(attrs={
                'min': 1, 'max': 5, 'class': 'w-16 p-1 border rounded'
            })
        }

