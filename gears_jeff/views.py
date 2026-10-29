
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from .models import (
    Personaje,
    Escuadron,
    Arma,
    Enemigo,
    Campana,
    Juego,
)

from .forms import (
    PersonajeForm,
    EscuadronForm,
    ArmaForm,
    EnemigoForm,
    CampanaForm,
    JuegoForm,
)


# ==========================================
# INICIO
# ==========================================

def inicio(request):
    modulos = [
        {
            "numero": "01",
            "icono": "✹",
            "nombre": "Personajes",
            "descripcion": "Conoce a los soldados que defienden el universo.",
            "url": reverse("gears_jeff:personajes"),
            "clase": "personajes",
            "imagen": "gears_jeff/img/fondo-gears.jpg",
        },
        {
            "numero": "02",
            "icono": "🛡️",
            "nombre": "Escuadrones",
            "descripcion": "Explora las unidades de combate.",
            "url": reverse("gears_jeff:escuadrones"),
            "clase": "escuadrones",
            "color": "#8c1717",
            "imagen": "gears_jeff/img/escuadrones.png",
        },
        {
            "numero": "03",
            "icono": "⚔️",
            "nombre": "Arsenal",
            "descripcion": "Descubre las armas de la CGO.",
            "url": reverse("gears_jeff:arsenal"),
            "clase": "arsenal",
            "color": "#b88746",
            "imagen": "gears_jeff/img/armas.png",
        },
        {
            "numero": "04",
            "icono": "☠️",
            "nombre": "Enemigos",
            "descripcion": "Identifica las amenazas de Sera.",
            "url": reverse("gears_jeff:enemigos"),
            "clase": "enemigos",
            "color": "#6b2020",
            "imagen": "gears_jeff/img/enemigos.png",
        },
        {
            "numero": "05",
            "icono": "🎖️",
            "nombre": "Campañas",
            "descripcion": "Revive las misiones más importantes.",
            "url": reverse("gears_jeff:campanas"),
            "clase": "campanas",
            "color": "#65734b",
            "imagen": "gears_jeff/img/campaña.png",
        },
        {
            "numero": "06",
            "icono": "🎮",
            "nombre": "Juegos",
            "descripcion": "Explora los títulos de la saga.",
            "url": reverse("gears_jeff:juegos"),
            "clase": "juegos",
            "color": "#526c85",
            "imagen": "gears_jeff/img/juegos.png",
        },
    ]

    return render(
        request,
        "gears_jeff/inicio.html",
        {"modulos": modulos},
    )


# ==========================================
# LISTADOS
# ==========================================

def personajes(request):
    return render(
        request,
        "gears_jeff/personajes.html",
        {"personajes": Personaje.objects.all()},
    )


def escuadrones(request):
    return render(
        request,
        "gears_jeff/escuadrones.html",
        {"escuadrones": Escuadron.objects.all()},
    )


def arsenal(request):
    return render(
        request,
        "gears_jeff/arsenal.html",
        {"armas": Arma.objects.all()},
    )


def enemigos(request):
    return render(
        request,
        "gears_jeff/enemigos.html",
        {"enemigos": Enemigo.objects.all()},
    )


def campanas(request):
    return render(
        request,
        "gears_jeff/campanas.html",
        {"campanas": Campana.objects.all()},
    )


def juegos(request):
    return render(
        request,
        "gears_jeff/juegos.html",
        {"juegos": Juego.objects.all()},
    )


# ==========================================
# CREAR REGISTROS
# ==========================================

def procesar_formulario(
    request,
    formulario,
    titulo,
    descripcion,
    nombre_url_lista,
):
    url_lista = reverse(nombre_url_lista)

    if request.method == "POST":
        form = formulario(request.POST, request.FILES)

        if form.is_valid():
            registro = form.save()

            messages.success(
                request,
                f'"{registro}" se registró correctamente.',
            )

            return redirect(url_lista)
    else:
        form = formulario()

    return render(
        request,
        "gears_jeff/formulario_modulo.html",
        {
            "form": form,
            "titulo_formulario": titulo,
            "descripcion_formulario": descripcion,
            "url_lista": url_lista,
        },
    )


def crear_personaje(request):
    return procesar_formulario(
        request,
        PersonajeForm,
        "Registrar personaje",
        "Añade un nuevo personaje a los archivos de Sera.",
        "gears_jeff:personajes",
    )


def crear_escuadron(request):
    return procesar_formulario(
        request,
        EscuadronForm,
        "Crear escuadrón",
        "Registra un equipo, su líder y sus integrantes.",
        "gears_jeff:escuadrones",
    )


def crear_arma(request):
    return procesar_formulario(
        request,
        ArmaForm,
        "Registrar arma",
        "Añade una nueva arma al arsenal de la CGO.",
        "gears_jeff:arsenal",
    )


def crear_enemigo(request):
    return procesar_formulario(
        request,
        EnemigoForm,
        "Registrar enemigo",
        "Añade una nueva amenaza a los archivos de Sera.",
        "gears_jeff:enemigos",
    )


def crear_juego(request):
    return procesar_formulario(
        request,
        JuegoForm,
        "Registrar juego",
        "Añade un título a la biblioteca de Gears of War.",
        "gears_jeff:juegos",
    )


def crear_campana(request):
    return procesar_formulario(
        request,
        CampanaForm,
        "Registrar campaña",
        "Registra una campaña y relaciónala con su juego.",
        "gears_jeff:campanas",
    )


# ==========================================
# EDITAR PERSONAJE
# ==========================================

def editar_personaje(request, personaje_id):
    personaje = get_object_or_404(Personaje, id=personaje_id)

    if request.method == "POST":
        form = PersonajeForm(
            request.POST,
            request.FILES,
            instance=personaje,
        )

        if form.is_valid():
            registro = form.save()

            messages.success(
                request,
                f'"{registro}" se actualizó correctamente.',
            )

            return redirect("gears_jeff:personajes")
    else:
        form = PersonajeForm(instance=personaje)

    return render(
        request,
        "gears_jeff/formulario_modulo.html",
        {
            "form": form,
            "titulo_formulario": "Editar personaje",
            "descripcion_formulario": "Modifica la información del personaje.",
            "url_lista": reverse("gears_jeff:personajes"),
        },
    )


# ==========================================
# EDITAR OTROS REGISTROS
# ==========================================

def procesar_edicion(
    request,
    modelo,
    formulario,
    registro_id,
    titulo,
    descripcion,
    nombre_url_lista,
):
    registro = get_object_or_404(modelo, id=registro_id)
    url_lista = reverse(nombre_url_lista)

    if request.method == "POST":
        form = formulario(
            request.POST,
            request.FILES,
            instance=registro,
        )

        if form.is_valid():
            registro_actualizado = form.save()

            messages.success(
                request,
                f'"{registro_actualizado}" se actualizó correctamente.',
            )

            return redirect(url_lista)
    else:
        form = formulario(instance=registro)

    return render(
        request,
        "gears_jeff/formulario_modulo.html",
        {
            "form": form,
            "titulo_formulario": titulo,
            "descripcion_formulario": descripcion,
            "url_lista": url_lista,
        },
    )


def editar_escuadron(request, escuadron_id):
    return procesar_edicion(
        request,
        Escuadron,
        EscuadronForm,
        escuadron_id,
        "Editar escuadrón",
        "Modifica la información de la unidad de combate.",
        "gears_jeff:escuadrones",
    )


def editar_arma(request, arma_id):
    return procesar_edicion(
        request,
        Arma,
        ArmaForm,
        arma_id,
        "Editar arma",
        "Modifica la información del arma del arsenal.",
        "gears_jeff:arsenal",
    )


def editar_enemigo(request, enemigo_id):
    return procesar_edicion(
        request,
        Enemigo,
        EnemigoForm,
        enemigo_id,
        "Editar enemigo",
        "Modifica la información de la amenaza.",
        "gears_jeff:enemigos",
    )


def editar_campana(request, campana_id):
    return procesar_edicion(
        request,
        Campana,
        CampanaForm,
        campana_id,
        "Editar campaña",
        "Modifica la información de la campaña.",
        "gears_jeff:campanas",
    )


def editar_juego(request, juego_id):
    return procesar_edicion(
        request,
        Juego,
        JuegoForm,
        juego_id,
        "Editar juego",
        "Modifica la información del título.",
        "gears_jeff:juegos",
    )


# ==========================================
# ELIMINAR REGISTROS
# ==========================================

def procesar_eliminacion(
    request,
    modelo,
    registro_id,
    nombre_modulo,
    nombre_url_lista,
):
    registro = get_object_or_404(modelo, id=registro_id)
    nombre_registro = str(registro)
    url_lista = reverse(nombre_url_lista)

    if request.method == "POST":
        registro.delete()

        messages.success(
            request,
            f'{nombre_modulo.capitalize()}: "{nombre_registro}" '
            f'fue eliminado correctamente.',
        )

        return redirect(url_lista)

    return render(
        request,
        "gears_jeff/eliminar.html",
        {
            "objeto": registro,
            "modulo": nombre_modulo,
            "url_lista": url_lista,
        },
    )


def eliminar_personaje(request, personaje_id):
    return procesar_eliminacion(
        request,
        Personaje,
        personaje_id,
        "personajes",
        "gears_jeff:personajes",
    )


def eliminar_escuadron(request, escuadron_id):
    return procesar_eliminacion(
        request,
        Escuadron,
        escuadron_id,
        "escuadrones",
        "gears_jeff:escuadrones",
    )


def eliminar_arma(request, arma_id):
    return procesar_eliminacion(
        request,
        Arma,
        arma_id,
        "arsenal",
        "gears_jeff:arsenal",
    )


def eliminar_enemigo(request, enemigo_id):
    return procesar_eliminacion(
        request,
        Enemigo,
        enemigo_id,
        "enemigos",
        "gears_jeff:enemigos",
    )


def eliminar_campana(request, campana_id):
    return procesar_eliminacion(
        request,
        Campana,
        campana_id,
        "campañas",
        "gears_jeff:campanas",
    )


def eliminar_juego(request, juego_id):
    return procesar_eliminacion(
        request,
        Juego,
        juego_id,
        "juegos",
        "gears_jeff:juegos",
    )
