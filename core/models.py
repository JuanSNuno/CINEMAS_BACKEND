from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


# Función validadora (Principio DRY)
def validate_email_format(value):
    """Valida que el email contenga un @."""
    if '@' not in value:
        raise ValidationError('El formato del email no es válido.')

class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    fecha_registro = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['usuario_id']

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    pelicula_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    sinopsis = models.TextField(null=True, blank=True)
    genero = models.CharField(max_length=50, null=True, blank=True)
    duracion_minutos = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = 'peliculas'
        verbose_name = 'Película'
        verbose_name_plural = 'Películas'
        ordering = ['pelicula_id']
    
    def __str__(self):
        return self.titulo

class Funcion(models.Model):
    funcion_id = models.AutoField(primary_key=True)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    sala = models.CharField(max_length=10)
    fecha_hora = models.DateTimeField()
    
    class Meta:
        db_table = 'funciones'
        verbose_name = 'Función'
        verbose_name_plural = 'Funciones'
        ordering = ['funcion_id']
    
    def __str__(self):
        return f'{self.pelicula.titulo} - {self.fecha_hora} - {self.sala}'

class Reserva(models.Model):
    reserva_id = models.AutoField(primary_key=True)
    funcion = models.ForeignKey(Funcion, on_delete=models.RESTRICT)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cantidad_asientos = models.IntegerField()
    fecha_reserva = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'reservas'
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['reserva_id']

    def __str__(self):
        return f'Reserva de {self.usuario.nombre} para {self.funcion}'