
from django.contrib import admin
from .models import Personaje, Escuadron, Arma, Enemigo, Juego, Campana


@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    list_display = ("nombre", "alias", "rango", "afiliacion", "activo")
    list_filter = ("activo", "afiliacion")
    search_fields = ("nombre", "alias", "biografia")
    list_editable = ("activo",)


@admin.register(Escuadron)
class EscuadronAdmin(admin.ModelAdmin):
    list_display = ("nombre", "lider", "mision", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre", "mision", "descripcion")
    filter_horizontal = ("integrantes",)


@admin.register(Arma)
class ArmaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "dano", "disponible")
    list_filter = ("categoria", "disponible")
    search_fields = ("nombre", "descripcion")


@admin.register(Enemigo)
class EnemigoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "especie", "peligrosidad", "activo")
    list_filter = ("peligrosidad", "activo")
    search_fields = ("nombre", "especie", "descripcion")


@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha_lanzamiento", "activo")
    list_filter = ("activo",)
    search_fields = ("titulo", "descripcion")


@admin.register(Campana)
class CampanaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "juego", "capitulos", "activa")
    list_filter = ("activa", "juego")
    search_fields = ("titulo", "sinopsis", "ubicacion")
