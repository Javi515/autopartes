"""Configuración de URLs para el proyecto Autoparts.

La lista `urlpatterns` dirige las URLs hacia las vistas correspondientes. Para más información, visita:
https://docs.djangoproject.com/en/3.0/topics/http/urls/

Ejemplos:
Vistas basadas en funciones:
    1. Agrega una importación:  from my_app import views
    2. Agrega una ruta:  path('', views.home, name='home')

Vistas basadas en clases:
    1. Agrega una importación:  from other_app.views import Home
    2. Agrega una ruta:  path('', Home.as_view(), name='home')

Incluyendo otras configuraciones de URLs:
    1. Importa la función include(): from django.urls import include, path
    2. Agrega una ruta:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Rutas principales del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),  # Panel de administración
    path('accounts/', include("accounts.urls")),  # Rutas de cuentas/usuarios
    path('orders/', include("orders.urls")),      # Rutas para pedidos
    path('', include("parts.urls"))               # Página principal del sitio (partes)
]

# Configuración para servir archivos multimedia en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
