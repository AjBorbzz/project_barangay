from django.urls import path

from . import views

urlpatterns = [
    path('manage_profile', views.manage_profile, name='manage_profile'),
    path('accounts_view', views.accounts_view, name='accounts_view'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]