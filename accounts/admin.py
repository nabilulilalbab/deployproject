from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'role', 'is_verified', 'is_staff']  # ✅ tampilkan di list
    list_filter = ['role', 'is_verified']  # ✅ filter di sidebar admin

    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('role', 'no_hp', 'alamat', 'nik', 'foto_ktp', 'selfie_ktp', 'tanggal_lahir', 'is_verified')
        }),
    )

admin.site.register(User, CustomUserAdmin)
