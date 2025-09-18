# cine/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Pelicula, Usuario, Reserva, Funcion
from .serializers import (
    PeliculaSerializer, 
    UsuarioSerializer, 
    ReservaSerializer, 
    CrearReservaSerializer,
    FuncionSerializer,
    CrearFuncionSerializer
)

# Vista para listar y crear películas (Principio OCP: Abierto a extensión)
class PeliculaListCreateView(generics.ListCreateAPIView):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

# Vista para listar y registrar usuarios
class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Vista para listar y crear funciones
class FuncionListCreateView(generics.ListCreateAPIView):
    queryset = Funcion.objects.all().select_related('pelicula')
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CrearFuncionSerializer
        return FuncionSerializer

# Vista para ver todas las reservas y crear una nueva (Principio KISS)
class ReservaListCreateView(generics.ListCreateAPIView):
    queryset = Reserva.objects.all().select_related('usuario', 'funcion__pelicula')

    # SoC: Lógica diferente para obtener (GET) y crear (POST)
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CrearReservaSerializer # Usa el serializer simple para la entrada
        return ReservaSerializer # Usa el serializer detallado para la salida

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Lógica de reserva simplificada gracias al ORM
        usuario_id = serializer.validated_data['usuario'].usuario_id
        
        # Verificar si es reserva por película o función
        if 'funcion' in serializer.validated_data and serializer.validated_data['funcion']:
            funcion_id = serializer.validated_data['funcion'].funcion_id
            # Validamos que no exista una reserva igual para la función
            if Reserva.objects.filter(usuario_id=usuario_id, funcion_id=funcion_id).exists():
                return Response(
                    {"error": "Ya tienes una reserva para esta función."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        elif 'pelicula' in serializer.validated_data and serializer.validated_data['pelicula']:
            pelicula_id = serializer.validated_data['pelicula'].pelicula_id
            # Validamos que no exista una reserva igual para la película
            if Reserva.objects.filter(usuario_id=usuario_id, funcion__pelicula_id=pelicula_id).exists():
                return Response(
                    {"error": "Ya tienes una reserva para esta película."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)