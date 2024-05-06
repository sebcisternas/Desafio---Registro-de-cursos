from app.models import Curso,Estudiante,Profesor,Direccion

def crear_curso (codigo,nombre,version):
    curso = Curso(codigo=codigo,nombre=nombre,version=version)
    curso.save()
    print("Se ha creado el Curso")
    return curso

def crear_profesor (rut,nombre,apellido,creacion_registro, modificacion_registro, creado_por,activo=False):
    profesor = Profesor(rut=rut,nombre=nombre,apellido=apellido,activo=activo,creacion_registro=creacion_registro,modificacion_registro=modificacion_registro,creado_por=creado_por)
    profesor.save()
    print("Se ha creado el Profesor")
    return profesor

def crear_estudiante (rut,nombre,apellido,fech_nac,creacion_registro, modificacion_registro, creado_por,activo=False):
    estudiante = Estudiante(rut=rut,nombre=nombre,apellido=apellido,fech_nac=fech_nac, activo=activo,creacion_registro=creacion_registro,modificacion_registro=modificacion_registro,creado_por=creado_por)
    estudiante.save()
    print("Se ha creado el Estudiante")
    return estudiante

def crear_direccion(calle,numero,dpto,comuna,ciudad,region):
    direccion = Direccion(calle=calle,numero=numero,dpto=dpto,comuna=comuna,ciudad=ciudad,region=region)
    direccion.save()
    print("Se ha creado la Direccion")
    return direccion

def obtener_estudiante(rut):
    if Estudiante.objects.filter(rut=rut).exists():
        estudiante = Estudiante.objects.get(rut=rut)
        print("Se ha encontrado el Estudiante")
        return estudiante
    else:
        print("No se ha encontrado el Estudiante")
        return None
    
def obtener_profesor(rut):
    if Profesor.objects.filter(rut=rut).exists():
        profesor = Profesor.objects.get(rut=rut)
        print("Se ha encontrado el Profesor")
        return profesor
    else:
        print("No se ha encontrado el Profesor")
        return None
    
def obtener_curso(codigo):
    if Curso.objects.filter(codigo=codigo).exists():
        curso = Curso.objects.get(codigo=codigo)
        print("Se ha encontrado el Curso")
        return curso
    else:
        print("No se ha encontrado el Curso")
        return None
    
def agregar_profesor_a_curso(codigo,rut):
    profesor = obtener_profesor(rut)
    curso = obtener_curso(codigo)

    curso.profesor_set.add(profesor)
    curso.save()
    print("Se ha agregado el Profesor al Curso")
    
def agregar_cursos_a_estudiantes(rut,codigos):
    estudiante = obtener_estudiante(rut)
    for codigo in codigos:
        curso = obtener_curso(codigo)
        estudiante.curso_set.add(curso)
        estudiante.save()
    print("Se ha agregado los Cursos al Estudiante")
    









