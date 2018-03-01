from django.db import models

# Create your models here.
class Alumno(models.Model):
	Cuenta= models.CharField(max_length=8)
	Nombre= models.CharField(max_length=35)
	Ap_paterno = models.CharField(max_length=35)
	Ap_materno = models.CharField(max_length=35)
	Edad = 	models.CharField(max_length=2)
	FechaNacimiento = models.DateField()
	SEXOS = (('F','Fememino'),('M','Masculino'))
	Sexo = models.CharField(max_length=1, choices=SEXOS, default='M')

	def __str__(self):
		return self.Nombre