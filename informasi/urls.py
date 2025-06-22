from django.urls import path
from . import views

app_name = 'informasi'

urlpatterns = [
    path('tentang-kami/', views.about_us_view, name='tentang_kami'),
    path('kontak/', views.contact_view, name='kontak'),
    path('kebijakan-privasi/', views.privacy_policy_view, name='kebijakan_privasi'),
]
