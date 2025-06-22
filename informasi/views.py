from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Page, TeamMember
from .forms import ContactForm

def about_us_view(request):
    """Menampilkan halaman 'Tentang Kami'."""
    page = get_object_or_404(Page, slug='tentang-kami', is_published=True)
    team_members = TeamMember.objects.all()
    context = {
        'page': page,
        'team_members': team_members,
    }
    return render(request, 'informasi/tentang_kami.html', context)

def contact_view(request):
    """Menampilkan halaman kontak dan memproses form."""
    page = get_object_or_404(Page, slug='kontak', is_published=True)
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Terima kasih! Pesan Anda telah berhasil terkirim.')
            return redirect('informasi:kontak')
    else:
        form = ContactForm()

    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'informasi/kontak.html', context)

def privacy_policy_view(request):
    """Menampilkan halaman 'Kebijakan Privasi'."""
    page = get_object_or_404(Page, slug='kebijakan-privasi', is_published=True)
    context = {
        'page': page,
    }
    return render(request, 'informasi/page_detail.html', context)
