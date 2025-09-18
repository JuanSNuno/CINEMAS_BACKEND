# cine/urls.py
from django.urls import path
from .views import (
    PeliculaListCreateView,
    UsuarioListCreateView,
    ReservaListCreateView,
    FuncionListCreateView
)

urlpatterns = [
    path('peliculas/', PeliculaListCreateView.as_view(), name='lista-peliculas'),
    path('usuarios/', UsuarioListCreateView.as_view(), name='lista-usuarios'),
    path('reservas/', ReservaListCreateView.as_view(), name='lista-reservas'),
    path('funciones/', FuncionListCreateView.as_view(), name='lista-funciones'),
]