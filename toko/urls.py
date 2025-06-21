from django.urls import path
from . import views

app_name='toko'
urlpatterns = [
    path('temukan/', views.toko_leaflet_page, name='toko_leaflet_page'),
    # path('terdekat/', views.toko_terdekat, name='toko_terdekat_api'),
    path('tambah/', views.tambah_toko, name='tambah_toko'),
    path('cari/', views.cari_toko, name='cari_toko'),
    path('dashboard/', views.dashboard_mitra, name='dashboard_mitra'),
    path('produk/tambah/', views.tambah_produk, name='tambah_produk'),
    path('produk/edit/<int:pk>/', views.edit_produk, name='edit_produk'),
    path('produk/hapus/<int:pk>/', views.hapus_produk, name='hapus_produk'),
    path('toko/<int:pk>/', views.detail_toko, name='detail_toko'),
]
