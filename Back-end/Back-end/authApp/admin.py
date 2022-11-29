from django.contrib import admin
from .models.user import User
from .models.empleados import Empleados
from .models.pacientes import Pacientes
from .models.familiar import Familiares
from .models.historiaclinica import Historia_Clinica
from .models.signosvitales import SignosVitales

# Register your models here.
admin.site.register(User)
admin.site.register(Empleados)
admin.site.register(Pacientes)
admin.site.register(Historia_Clinica)
admin.site.register(SignosVitales)
admin.site.register(Familiares)
