from django.urls import path
from .views import user_register, mitra_register, CustomLoginView
from django.contrib.auth.views import LogoutView


app_name = 'accounts'
urlpatterns = [
    path('login/user/', CustomLoginView.as_view(extra_context={'title': 'Login User'}), name='login_user'),
    path('login/mitra/', CustomLoginView.as_view(extra_context={'title': 'Login Mitra'}), name='login_mitra'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/user/', user_register, name='register_user'),
    path('register/mitra/', mitra_register, name='register_mitra'),
]
