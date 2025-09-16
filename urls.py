# cinemas_backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Añade esta línea para conectar las URLs de tu app 'cine'
    path('api/', include('cine.urls')), 
]