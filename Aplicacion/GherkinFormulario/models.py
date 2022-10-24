from django.db import models

# Create your models here.

class CasoPrueba(models.Model):
    CPNombre = models.CharField(max_length = 255)

class CPAtributo(models.Model):
    CPAtributo = models.CharField(max_length = 255)

class AtributosCasoPrueba(models.Model):
    CPAtributoFK = models.ForeignKey(CPAtributo, null=True, on_delete=models.CASCADE)
    CPValorAtributo = models.CharField(max_length = 255)
    CasoPruebaFK = models.ForeignKey(CasoPrueba, null=True, on_delete=models.CASCADE)

class LenguajeGherkin(models.Model):
    SentenciaNombre = models.CharField(max_length = 255)

class PseudoAlgoritmoCasoPrueba(models.Model):
    LenguajeGherkinFK = models.ForeignKey(LenguajeGherkin, null=True, on_delete=models.CASCADE)
    CPPaso = models.CharField(max_length = 255)
    CPResultado = models.CharField(max_length = 255)