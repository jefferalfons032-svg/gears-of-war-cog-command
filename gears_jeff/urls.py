
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "gears_jeff"

urlpatterns = [
    # Página principal
    path("", views.inicio, name="inicio"),

    # Módulos principales
    path("personajes/", views.personajes, name="personajes"),
    path("escuadrones/", views.escuadrones, name="escuadrones"),
    path("arsenal/", views.arsenal, name="arsenal"),
    path("enemigos/", views.enemigos, name="enemigos"),
    path("campanas/", views.campanas, name="campanas"),
    path("juegos/", views.juegos, name="juegos"),

    # Crear personajes
    path(
        "personajes/crear/",
        views.crear_personaje,
        name="crear_personaje",
    ),

    # Editar personajes
    path(
        "editar_personaje/<int:personaje_id>/",
        views.editar_personaje,
        name="editar_personaje",
    ),

    # Eliminar personajes
    path(
        "personajes/eliminar/<int:personaje_id>/",
        views.eliminar_personaje,
        name="eliminar_personaje",
    ),

    # Crear escuadrones
    path(
        "escuadrones/crear/",
        views.crear_escuadron,
        name="crear_escuadron",
    ),

    # Editar escuadrones
    path(
        "escuadrones/editar/<int:escuadron_id>/",
        views.editar_escuadron,
        name="editar_escuadron",
    ),

    # Eliminar escuadrones
    path(
        "escuadrones/eliminar/<int:escuadron_id>/",
        views.eliminar_escuadron,
        name="eliminar_escuadron",
    ),

    # Crear armas
    path(
        "arsenal/crear/",
        views.crear_arma,
        name="crear_arma",
    ),

    # Editar armas
    path(
        "arsenal/editar/<int:arma_id>/",
        views.editar_arma,
        name="editar_arma",
    ),

    # Eliminar armas
    path(
        "arsenal/eliminar/<int:arma_id>/",
        views.eliminar_arma,
        name="eliminar_arma",
    ),

    # Crear enemigos
    path(
        "enemigos/crear/",
        views.crear_enemigo,
        name="crear_enemigo",
    ),

    # Editar enemigos
    path(
        "enemigos/editar/<int:enemigo_id>/",
        views.editar_enemigo,
        name="editar_enemigo",
    ),

    # Eliminar enemigos
    path(
        "enemigos/eliminar/<int:enemigo_id>/",
        views.eliminar_enemigo,
        name="eliminar_enemigo",
    ),

    # Crear campañas
    path(
        "campanas/crear/",
        views.crear_campana,
        name="crear_campana",
    ),

    # Editar campañas
    path(
        "campanas/editar/<int:campana_id>/",
        views.editar_campana,
        name="editar_campana",
    ),

    # Eliminar campañas
    path(
        "campanas/eliminar/<int:campana_id>/",
        views.eliminar_campana,
        name="eliminar_campana",
    ),

    # Crear juegos
    path(
        "juegos/crear/",
        views.crear_juego,
        name="crear_juego",
    ),

    # Editar juegos
    path(
        "juegos/editar/<int:juego_id>/",
        views.editar_juego,
        name="editar_juego",
    ),

    # Eliminar juegos
    path(
        "juegos/eliminar/<int:juego_id>/",
        views.eliminar_juego,
        name="eliminar_juego",
    ),
]

# Archivos multimedia durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
