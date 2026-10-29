
from django.db import models


class Personaje(models.Model):
    nombre = models.CharField(max_length=120)
    alias = models.CharField(max_length=120, blank=True)
    biografia = models.TextField()
    rango = models.CharField(max_length=100, blank=True)
    afiliacion = models.CharField(max_length=120, blank=True)
    imagen = models.ImageField(upload_to="gears/personajes/", blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Personaje"
        verbose_name_plural = "Personajes"

    def __str__(self):
        return self.nombre


class Escuadron(models.Model):
    nombre = models.CharField(max_length=120)
    lider = models.ForeignKey(
        "Personaje",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="escuadrones_liderados",
    )
    integrantes = models.ManyToManyField(
        "Personaje", blank=True, related_name="escuadrones"
    )
    mision = models.CharField(max_length=200, blank=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="gears/escuadrones/", blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Escuadrón"
        verbose_name_plural = "Escuadrones"

    def __str__(self):
        return self.nombre


class Arma(models.Model):
    CATEGORIAS = [
        ("asalto", "Fusil de asalto"),
        ("pesada", "Arma pesada"),
        ("explosiva", "Explosiva"),
        ("cuerpo", "Combate cuerpo a cuerpo"),
        ("otra", "Otra"),
    ]

    nombre = models.CharField(max_length=120)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default="otra")
    descripcion = models.TextField()
    dano = models.PositiveSmallIntegerField(default=0)
    municion = models.CharField(max_length=100, blank=True)
    imagen = models.ImageField(upload_to="gears/arsenal/", blank=True, null=True)
    disponible = models.BooleanField(default=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Arma"
        verbose_name_plural = "Arsenal"

    def __str__(self):
        return self.nombre


class Enemigo(models.Model):
    NIVELES = [
        ("bajo", "Bajo"),
        ("medio", "Medio"),
        ("alto", "Alto"),
        ("critico", "Crítico"),
    ]

    nombre = models.CharField(max_length=120)
    especie = models.CharField(max_length=120, blank=True)
    peligrosidad = models.CharField(max_length=20, choices=NIVELES, default="medio")
    habilidades = models.TextField(blank=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="gears/enemigos/", blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Enemigo"
        verbose_name_plural = "Enemigos"

    def __str__(self):
        return self.nombre


class Juego(models.Model):
    titulo = models.CharField(max_length=150)
    fecha_lanzamiento = models.DateField(blank=True, null=True)
    plataformas = models.CharField(max_length=200, blank=True)
    clasificacion = models.CharField(max_length=50, blank=True)
    descripcion = models.TextField()
    portada = models.ImageField(upload_to="gears/juegos/", blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["titulo"]
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"

    def __str__(self):
        return self.titulo


class Campana(models.Model):
    titulo = models.CharField(max_length=150)
    juego = models.ForeignKey(
        Juego, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="campanas",
    )
    capitulos = models.PositiveSmallIntegerField(default=1)
    ubicacion = models.CharField(max_length=150, blank=True)
    sinopsis = models.TextField()
    imagen = models.ImageField(upload_to="gears/campanas/", blank=True, null=True)
    activa = models.BooleanField(default=True)

    class Meta:
        ordering = ["titulo"]
        verbose_name = "Campaña"
        verbose_name_plural = "Campañas"

    def __str__(self):
        return self.titulo
