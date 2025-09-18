from django.db import models
from django.core.exceptions import ValidationError

# Función validadora (Principio DRY)
def validate_email_format(value):
    """Valida que el email contenga un @."""
    if '@' not in value:
        raise ValidationError('El formato del email no es válido.')

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    # Usamos un validador para mantener la lógica limpia (DRY)
    email = models.EmailField(max_length=100, unique=True, validators=[validate_email_format])

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    # Relaciones claras entre modelos (Cohesión)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reserva de {self.usuario.nombre} para {self.pelicula.titulo}'