
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Panel de administración
    path("admin/", admin.site.urls),

    # Página principal y módulos de COG COMMAND
    path("", include("gears_jeff.urls")),
]


# Mostrar imágenes subidas durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
