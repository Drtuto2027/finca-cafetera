from django.contrib import admin
from django.urls import path, include

# Personalizar admin
admin.site.site_header = "☕ Sistema de Gestión Cafetera"
admin.site.site_title = "Administración Finca Café"
admin.site.index_title = "Panel de Control Principal"

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]
