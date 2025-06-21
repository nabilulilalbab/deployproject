from django.http import JsonResponse
from .models import Toko, Produk, KomentarToko
from math import radians, cos, sin, asin, sqrt
from django.shortcuts import render, redirect,get_object_or_404
from .forms import TokoForm,ProdukForm, KomentarTokoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    return R * c


def toko_leaflet_page(request):
    return render(request, 'toko/temukan_toko.html')



@login_required
def tambah_toko(request):
    if request.user.role != 'mitra':
        return HttpResponseForbidden("Hanya pengguna dengan role 'mitra' yang dapat menambahkan toko.")

    # Cegah duplikasi
    if Toko.objects.filter(user=request.user).exists():
        return HttpResponseForbidden("Anda sudah memiliki toko.")

    if request.method == 'POST':
        form = TokoForm(request.POST)
        if form.is_valid():
            toko = form.save(commit=False)
            toko.user = request.user
            toko.save()
            return redirect('toko:dashboard_mitra')
    else:
        form = TokoForm()
    
    return render(request, 'toko/tambah_toko.html', {'form': form})



def cari_toko(request):
    nama = request.GET.get('nama', '')
    kabupaten = request.GET.get('kabupaten', '')
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    radius = float(request.GET.get('radius', 25))

    queryset = Toko.objects.all()

    if nama:
        queryset = queryset.filter(nama__icontains=nama)

    if kabupaten:
        queryset = queryset.filter(kabupaten__icontains=kabupaten)

    hasil = []
    for toko in queryset:
        if lat and lon:
            jarak = haversine(float(lat), float(lon), toko.latitude, toko.longitude)
            if jarak > radius:
                continue
        else:
            jarak = None

        hasil.append({
            'id' : toko.id,
            'nama': toko.nama,
            'alamat': toko.alamat,
            'kabupaten': toko.kabupaten,
            'latitude': toko.latitude,
            'longitude': toko.longitude,
            'jarak': round(jarak, 2) if jarak else None
        })

    return JsonResponse({'hasil': hasil})

@login_required
def dashboard_mitra(request):
    if request.user.role != 'mitra':
        return HttpResponseForbidden("Hanya mitra yang bisa mengakses dashboard ini")

    toko = Toko.objects.filter(user=request.user).first()
    produk = toko.produk.all() if toko else []
    return render(request, 'toko/dashboard_mitra.html', {'toko': toko, 'produk': produk})

@login_required
def tambah_produk(request):
    toko = get_object_or_404(Toko, user=request.user)
    if request.method == 'POST':
        form = ProdukForm(request.POST,  request.FILES)
        if form.is_valid():
            produk = form.save(commit=False)
            produk.toko = toko
            produk.save()
            return redirect('toko:dashboard_mitra')
    else:
        form = ProdukForm()
    return render(request, 'toko/tambah_produk.html', {'form': form})

@login_required
def edit_produk(request, pk):
    produk = get_object_or_404(Produk, pk=pk, toko__user=request.user)
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            return redirect('toko:dashboard_mitra')
    else:
        form = ProdukForm(instance=produk)
    return render(request, 'toko/edit_produk.html', {'form': form})

@login_required
def hapus_produk(request, pk):
    produk = get_object_or_404(Produk, pk=pk, toko__user=request.user)
    produk.delete()
    return redirect('toko:dashboard_mitra')


def detail_toko(request, pk):
    toko = get_object_or_404(Toko, pk=pk)
    produk = toko.produk.filter(is_active=True)
    komentar = toko.komentar.select_related('user').order_by('-tanggal')
    query = request.GET.get('q')
    if query:
        produk = produk.filter(nama__icontains=query)

    if request.method == 'POST' and request.user.is_authenticated:
        form = KomentarTokoForm(request.POST)
        if form.is_valid():
            komentar_baru = form.save(commit=False)
            komentar_baru.user = request.user
            komentar_baru.toko = toko
            komentar_baru.save()
            return redirect('toko:detail_toko', pk=toko.pk)
    else:
        form = KomentarTokoForm()

    return render(request, 'toko/detail_toko.html', {
        'toko': toko,
        'produk': produk,
        'query': query,
        'komentar': komentar,
        'form_komentar': form,
    })

