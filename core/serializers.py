# cine/serializers.py
from rest_framework import serializers
from .models import Pelicula, Usuario, Reserva, Funcion

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['usuario_id', 'nombre', 'email', 'fecha_registro']

class PeliculaSerializer(serializers.ModelSerializer):
    # Agregamos el campo id que es un alias para pelicula_id
    id = serializers.IntegerField(source='pelicula_id', read_only=True)
    
    class Meta:
        model = Pelicula
        fields = ['id', 'pelicula_id', 'titulo', 'sinopsis', 'genero', 'duracion_minutos']

class FuncionSerializer(serializers.ModelSerializer):
    pelicula_titulo = serializers.CharField(source='pelicula.titulo', read_only=True)
    # Agregamos el campo id que es un alias para funcion_id
    id = serializers.IntegerField(source='funcion_id', read_only=True)
    
    class Meta:
        model = Funcion
        fields = ['id', 'funcion_id', 'pelicula', 'pelicula_titulo', 'sala', 'fecha_hora']

class CrearFuncionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcion
        fields = ['pelicula', 'sala', 'fecha_hora']

class ReservaSerializer(serializers.ModelSerializer):
    # Para mostrar los nombres en lugar de solo los IDs
    usuario = serializers.StringRelatedField()
    funcion = FuncionSerializer(read_only=True)
    # Agregamos el campo id que es un alias para reserva_id
    id = serializers.IntegerField(source='reserva_id', read_only=True)
    
    class Meta:
        model = Reserva
        fields = ['id', 'reserva_id', 'usuario', 'funcion', 'fecha_reserva', 'cantidad_asientos']

class CrearReservaSerializer(serializers.ModelSerializer):
    # Este serializer es específico para la creación, esperando IDs.
    class Meta:
        model = Reserva
        fields = ['usuario', 'funcion', 'cantidad_asientos']