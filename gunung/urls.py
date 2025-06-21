from django.urls import path
from .views import home, daftar_gunung, detail_gunung


app_name = 'gunung'
urlpatterns = [
    path('', home, name='home'),
    path('gunung/', daftar_gunung, name='daftar'),
    path('gunung/<slug:slug>/', detail_gunung, name='detail'),
]
