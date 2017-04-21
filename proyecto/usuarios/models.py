# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


escolaridad = (
    ('M', 'Maestria'),
    ('D', 'Doctorado'),
)
tipos_actores = (
    ('ES', 'Estudiante'),
    ('TU', 'Tutor'),
    ('CO', 'Coordinador'),
    ('EV', 'Evaluador'),
    ('SE', 'Secretaria'),
)

class Filiacion(models.Model):
    filiacion_id = models.AutoField(primary_key=True)
    filiacion_universidad = models.CharField(max_length=50)
    filiacion_departamento= models.CharField(max_length=50)
    filiacion_grupo = models.CharField(max_length=50)

class Carrera(models.Model):
    # id_usuario = models.OneToOneField(User)
    carrera_id = models.AutoField(primary_key=True)
    carrera_codigo= models.CharField(max_length=10)
    carreras = (
        ('P', 'Maestria Profundización'),
        ('I', 'Maestria Investigación'),
        ('D', 'Doctorado'),
    )

    carrera_descripcion = models.CharField(max_length=1, choices=carreras)


class Rol_usuario(models.Model):
    rol_id=models.AutoField(primary_key=True)
    rol_tipo = models.CharField(max_length=2, choices=tipos_actores, default=1)

    def __str__(self):
        return str(self.rol_tipo)

User.add_to_class('rol', models.ForeignKey(Rol_usuario, default=1),)
# Create your models here.

class Persona(User):
    persona_id = models.AutoField(primary_key=True)
    persona_escolaridad= models.CharField(max_length=1, choices=escolaridad, blank=True)
    persona_filiacion= models.ForeignKey(Filiacion, blank=True, null=True)
    persona_es_coordinador= models.BooleanField
    persona_carrera=models.ForeignKey(Carrera, blank=True, null=True)


class Estado(models.Model):

    estado_id = models.AutoField(primary_key=True)
    estados_propuestas = (
        ('SO', 'Por_Someter'),
        ('AV', 'Por_Avalar'),
        ('EV', 'Por_Evaluar'),
        ('SU', 'Por_Sustentar'),
        ('FI', 'Finalizado'),
        ('AN', 'Anulado'),

    )
    estado_descripcion = models.CharField(max_length=2, choices=estados_propuestas)


class Propuesta(models.Model):

    propuesta_id= models.AutoField(primary_key=True)
    tipos_propuestas = (
        ('P', 'Maestria Profundización'),
        ('I', 'Maestria Investigación'),
        ('D', 'Doctorado'),
    )
    propuesta_tipo = models.CharField (max_length=1, choices=tipos_propuestas)
    propuesta_titulo = models.CharField(max_length=70)
    propuesta_estudiante = models.ForeignKey(Persona)
    propuesta_director = Persona
    codirector_propuesta = models.CharField(max_length=50)
    jurado1_propuesta= Persona
    jurado2_propuesta = Persona
    jurado3_propuesta = Persona(None)

    propuesta_estado =models.ForeignKey(Estado)
    observacion_propuesta= models.CharField

class Registro(models.Model):

    registro_id= models.AutoField(primary_key=True)
    registro_propuesta=models.ForeignKey(Propuesta)
    registro_fecha = models.DateTimeField(auto_now=True) #fecha en que inicia el estado
    registro_persona= models.ForeignKey(Persona) #Usuario encargado de la accion
    registro_estado_actual= models.ForeignKey(Estado)
    registro_aula= models.CharField(max_length=30, blank=True)
    registro_observaciones=models.CharField(max_length=200,blank=True)
    registro_hora_sustentacion=models.TimeField(null=True)
    registro_fecha_sustentacion=models.DateField(null=True)

# Estudiante hereda de usuario, por tanto hereda sus atributos


# Estudiante hereda de usuario, por tanto hereda sus atributos
