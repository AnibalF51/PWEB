from confi.wsgi import *

from core.erp.models import Type

# LISTAR

#query = Type.objects.all()

#print(query)

# INSERTAR

#t = Type()
#t.name = 'Hola'
#t.save()

# EDITAR

try:
    t = Type.objects.get(id=1)
    t.name = 'Hola123'
    t.save()
except Exception as e:
    print(e)

# ELIMINAR

#t= Type.objects.get(pk=1)
#t.delete()