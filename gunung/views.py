from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Gunung, Komentar
from .forms import KomentarForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Avg


def home(request):
    return render(request, 'gunung/home.html')

def daftar_gunung(request):
    query = request.GET.get('q')
    kategori = request.GET.get('kategori')

    gunung_list = Gunung.objects.all()

    if query:
        gunung_list = gunung_list.filter(nama__icontains=query)

    if kategori in ['easy', 'medium', 'hard']:
        gunung_list = gunung_list.filter(kategori=kategori)

    context = {
        'gunung_list': gunung_list,
        'kategori': kategori,
        'query': query
    }
    return render(request, 'gunung/daftar.html', context)

def detail_gunung(request, slug):
    gunung = get_object_or_404(Gunung, slug=slug)

    # Tambah 1 view
    gunung.views += 1
    gunung.save(update_fields=['views'])

    komentar_list = gunung.komentar.all().order_by('-created_at')

    # ⬇️ Di sini hitung rata-rata rating
    avg_rating = komentar_list.aggregate(Avg('rating'))['rating__avg']
    avg_rating = round(avg_rating, 1) if avg_rating else 0

    # Pagination komentar
    paginator = Paginator(komentar_list, 5)
    page = request.GET.get('page')
    komentar_page = paginator.get_page(page)

    if request.method == 'POST':
        form = KomentarForm(request.POST)
        if form.is_valid():
            komentar = form.save(commit=False)
            komentar.user = request.user
            komentar.gunung = gunung
            komentar.save()
            return redirect('gunung:detail', slug=slug)
    else:
        form = KomentarForm()

    return render(request, 'gunung/detail.html', {
        'gunung': gunung,
        'komentar': komentar_page,
        'form': form,
        'avg_rating': avg_rating,  # ⬅️ kirim ke template
    })
