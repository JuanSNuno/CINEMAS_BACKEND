# cine/urls.py
from django.urls import path
from .views import (
    PeliculaListCreateView,
    PeliculaDetailView,
    UsuarioListCreateView,
    UsuarioDetailView,
    ReservaListCreateView,
    ReservaDetailView,
    FuncionListCreateView,
    FuncionDetailView
)

urlpatterns = [
    # Rutas de lista y creación
    path('peliculas/', PeliculaListCreateView.as_view(), name='lista-peliculas'),
    path('usuarios/', UsuarioListCreateView.as_view(), name='lista-usuarios'),
    path('reservas/', ReservaListCreateView.as_view(), name='lista-reservas'),
    path('funciones/', FuncionListCreateView.as_view(), name='lista-funciones'),
    
    # Rutas de detalle (obtener, actualizar, eliminar)
    path('peliculas/<int:id>/', PeliculaDetailView.as_view(), name='detalle-pelicula'),
    path('usuarios/<int:id>/', UsuarioDetailView.as_view(), name='detalle-usuario'),
    path('reservas/<int:id>/', ReservaDetailView.as_view(), name='detalle-reserva'),
    path('funciones/<int:id>/', FuncionDetailView.as_view(), name='detalle-funcion'),
]