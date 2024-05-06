from django.db import models

# Create your models here.


class Direccion(models.Model):
    calle = models.CharField(max_length=50,null=False,blank=False)
    numero = models.CharField(max_length=10,null=False,blank=False)
    dpto = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50,null=False,blank=False)
    ciudad = models.CharField(max_length=50,null=False,blank=False)
    region = models.CharField(max_length=50,null=False,blank=False)
    
class Estudiante(models.Model):
    rut= models.CharField(max_length=9,primary_key=True,null=False)
    nombre = models.CharField(max_length=50,null=False,blank=False)
    apellido = models.CharField(max_length=50,null=False,blank=False)
    fecha_nac = models.DateField(null=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(null=False)
    modificacion_registro = models.DateField(null=False)
    creado_por = models.CharField(max_length=50,null=False,blank=False)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)
    
class Curso(models.Model):
    codigo = models.CharField(primary_key=True,max_length=10,null=True,unique=True)
    nombre = models.CharField(max_length=50,null=False,blank=False)
    version= models.IntegerField()
    

class Profesor(models.Model):
    rut= models.CharField(max_length=9,primary_key=True,null=False)
    nombre = models.CharField(max_length=50,null=False,blank=False)
    apellido = models.CharField(max_length=50,null=False,blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(null=False)
    modificacion_registro = models.DateField(null=False)
    creado_por = models.CharField(max_length=50,null=False,blank=False)
    cursos = models.ManyToManyField(Curso)
    
    
    