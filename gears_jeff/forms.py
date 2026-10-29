
from django import forms
from .models import (
    Personaje,
    Escuadron,
    Arma,
    Enemigo,
    Juego,
    Campana,
)


class EstiloFormulario:
    """Aplica el estilo visual a los campos de los formularios."""

    def aplicar_estilos(self):
        for nombre, campo in self.fields.items():
            if isinstance(campo.widget, forms.CheckboxInput):
                campo.widget.attrs.update({
                    "class": "campo-checkbox",
                })
            elif isinstance(campo.widget, forms.Select):
                campo.widget.attrs.update({
                    "class": "campo-formulario",
                })
            elif isinstance(campo.widget, forms.SelectMultiple):
                campo.widget.attrs.update({
                    "class": "campo-formulario campo-multiple",
                })
            elif isinstance(campo.widget, forms.ClearableFileInput):
                campo.widget.attrs.update({
                    "class": "campo-formulario",
                    "accept": "image/*",
                })
            elif isinstance(campo.widget, forms.Textarea):
                campo.widget.attrs.update({
                    "class": "campo-formulario",
                    "rows": 5,
                })
            else:
                campo.widget.attrs.update({
                    "class": "campo-formulario",
                })


class PersonajeForm(EstiloFormulario, forms.ModelForm):
    class Meta:
        model = Personaje
        fields = [
            "nombre", "alias", "biografia", "rango",
            "afiliacion", "imagen", "activo",
        ]
        labels = {
            "nombre": "Nombre del personaje",
            "alias": "Alias o apodo",
            "biografia": "Biografía",
            "rango": "Rango militar",
            "afiliacion": "Afiliación",
            "imagen": "Imagen del personaje",
            "activo": "Personaje activo",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Ej. Marcus Fenix",
                "autocomplete": "off",
            }),
            "alias": forms.TextInput(attrs={
                "placeholder": "Alias del personaje",
            }),
            "biografia": forms.Textarea(attrs={
                "placeholder": "Describe la historia del personaje",
            }),
            "rango": forms.TextInput(attrs={
                "placeholder": "Ej. Sargento",
            }),
            "afiliacion": forms.TextInput(attrs={
                "placeholder": "Ej. COG",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aplicar_estilos()

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"].strip()
        registros = Personaje.objects.filter(nombre__iexact=nombre)

        if self.instance.pk:
            registros = registros.exclude(pk=self.instance.pk)

        if registros.exists():
            raise forms.ValidationError(
                "Ya existe un personaje con ese nombre."
            )
        return nombre


class EscuadronForm(EstiloFormulario, forms.ModelForm):
    class Meta:
        model = Escuadron
        fields = [
            "nombre", "lider", "integrantes", "mision",
            "descripcion", "imagen", "activo",
        ]
        labels = {
            "nombre": "Nombre del escuadrón",
            "lider": "Líder del escuadrón",
            "integrantes": "Integrantes",
            "mision": "Misión asignada",
            "descripcion": "Descripción",
            "imagen": "Imagen del escuadrón",
            "activo": "Escuadrón activo",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Ej. Escuadrón Delta",
            }),
            "mision": forms.TextInput(attrs={
                "placeholder": "Objetivo de la misión",
            }),
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Describe las funciones del escuadrón",
            }),
            "integrantes": forms.SelectMultiple(attrs={
                "size": 6,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aplicar_estilos()
        self.fields["lider"].queryset = Personaje.objects.order_by("nombre")
        self.fields["integrantes"].queryset = Personaje.objects.order_by(
            "nombre"
        )


class ArmaForm(EstiloFormulario, forms.ModelForm):
    class Meta:
        model = Arma
        fields = [
            "nombre", "categoria", "descripcion",
            "dano", "municion", "imagen", "disponible",
        ]
        labels = {
            "nombre": "Nombre del arma",
            "categoria": "Categoría",
            "descripcion": "Descripción",
            "dano": "Daño",
            "municion": "Munición",
            "imagen": "Imagen del arma",
            "disponible": "Arma disponible",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Ej. Lancer",
            }),
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Describe las características del arma",
            }),
            "dano": forms.NumberInput(attrs={
                "min": 0,
                "placeholder": "Nivel de daño",
            }),
            "municion": forms.NumberInput(attrs={
                "min": 0,
                "placeholder": "Cantidad de munición",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aplicar_estilos()


class EnemigoForm(EstiloFormulario, forms.ModelForm):
    class Meta:
        model = Enemigo
        fields = [
            "nombre", "especie", "peligrosidad",
            "habilidades", "descripcion", "imagen", "activo",
        ]
        labels = {
            "nombre": "Nombre del enemigo",
            "especie": "Especie",
            "peligrosidad": "Nivel de peligrosidad",
            "habilidades": "Habilidades",
            "descripcion": "Descripción",
            "imagen": "Imagen del enemigo",
            "activo": "Enemigo activo",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Nombre del enemigo",
            }),
            "especie": forms.TextInput(attrs={
                "placeholder": "Ej. Locust",
            }),
            "habilidades": forms.Textarea(attrs={
                "placeholder": "Describe sus habilidades",
                "rows": 3,
            }),
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Características del enemigo",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aplicar_estilos()


class JuegoForm(EstiloFormulario, forms.ModelForm):
    class Meta:
        model = Juego
        fields = [
            "titulo", "fecha_lanzamiento", "plataformas",
            "clasificacion", "descripcion", "portada", "activo",
        ]
        labels = {
            "titulo": "Título del juego",
            "fecha_lanzamiento": "Fecha de lanzamiento",
            "plataformas": "Plataformas",
            "clasificacion": "Clasificación",
            "descripcion": "Descripción",
            "portada": "Portada del juego",
            "activo": "Juego activo",
        }
        widgets = {
            "titulo": forms.TextInput(attrs={
                "placeholder": "Ej. Gears of War",
            }),
            "fecha_lanzamiento": forms.DateInput(attrs={
                "type": "date",
            }),
            "plataformas": forms.TextInput(attrs={
                "placeholder": "Ej. Xbox, PC",
            }),
            "clasificacion": forms.TextInput(attrs={
                "placeholder": "Clasificación del juego",
            }),
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Describe el juego",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aplicar_estilos()


class CampanaForm(EstiloFormulario, forms.ModelForm):
    class Meta:
        model = Campana
        fields = [
            "titulo", "juego", "capitulos", "ubicacion",
            "sinopsis", "imagen", "activa",
        ]
        labels = {
            "titulo": "Título de la campaña",
            "juego": "Juego relacionado",
            "capitulos": "Cantidad de capítulos",
            "ubicacion": "Ubicación",
            "sinopsis": "Sinopsis",
            "imagen": "Imagen de la campaña",
            "activa": "Campaña activa",
        }
        widgets = {
            "titulo": forms.TextInput(attrs={
                "placeholder": "Nombre de la campaña",
            }),
            "capitulos": forms.NumberInput(attrs={
                "min": 1,
                "placeholder": "Cantidad de capítulos",
            }),
            "ubicacion": forms.TextInput(attrs={
                "placeholder": "Lugar donde ocurre",
            }),
            "sinopsis": forms.Textarea(attrs={
                "placeholder": "Describe la historia de la campaña",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aplicar_estilos()
        self.fields["juego"].queryset = Juego.objects.order_by("titulo")
