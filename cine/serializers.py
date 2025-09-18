# cine/serializers.py
from rest_framework import serializers
from .models import Pelicula, Usuario, Reserva

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__' # Incluye todos los campos del modelo

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'email']

class ReservaSerializer(serializers.ModelSerializer):
    # Para mostrar los nombres en lugar de solo los IDs
    usuario = serializers.StringRelatedField()
    pelicula = serializers.StringRelatedField()
    
    class Meta:
        model = Reserva
        fields = ['id', 'usuario', 'pelicula', 'fecha_reserva']

class CrearReservaSerializer(serializers.ModelSerializer):
    # Este serializer es específico para la creación, esperando IDs.
    class Meta:
        model = Reserva
        fields = ['usuario', 'pelicula']