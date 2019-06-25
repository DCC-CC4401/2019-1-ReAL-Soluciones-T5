from django.contrib import admin
from Alumnos.models import Alumno, Grupo, AlumnosGrupo

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Grupo)
admin.site.register(AlumnosGrupo)