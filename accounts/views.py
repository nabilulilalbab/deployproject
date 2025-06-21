from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, MitraRegisterForm, LoginForm
from django.contrib.auth.views import LoginView
from django.contrib import messages

def user_register(request):
    if request.user.is_authenticated:
        return redirect('gunung:home')  # atau bisa redirect sesuai role

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('gunung:home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register_user.html', {'form': form})

def mitra_register(request):
    if request.user.is_authenticated:
        if request.user.role == 'mitra':
            return redirect('toko:dashboard_mitra')
        else:
            return redirect('gunung:home')

    if request.method == 'POST':
        form = MitraRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'mitra'
            user.is_verified = False  # mitra belum diverifikasi
            user.save()
            return render(request, 'accounts/mitra_pending.html')  # tampilkan halaman menunggu verifikasi
    else:
        form = MitraRegisterForm()
    return render(request, 'accounts/register_mitra.html', {'form': form})




class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        user = form.get_user()
        if user.role == 'mitra' and not user.is_verified:
            messages.error(self.request, "Akun mitra Anda belum diverifikasi oleh admin.")
            return redirect('accounts:login_mitra')
        login(self.request, user)
        return redirect(self.get_success_url())

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == 'mitra':
                return redirect('toko:dashboard_mitra')
            else:
                return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        if self.request.user.role == 'mitra':
            return '/toko/dashboard/'
        else:
            return '/'

