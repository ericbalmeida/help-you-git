from django.db import models

def __str__(self):
    return self.nome

class TD_categorias(models.Model):
    nome = models.CharField(max_length=20)

class TB_psicologos(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField(11, primary_key=True)
    registro_crp = models.IntegerField(100)
    email = models.EmailField()
    senha = models.CharField(max_length=18)
    telefone = models.IntegerField(11)

class TB_salas(models.Model):
    cod_sala = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    admin = models.ForeignKey(TB_psicologos, on_delete=models.CASCADE)
    descricao = models.TextField()
    categoria = models.ForeignKey(TD_categorias, on_delete=models.CASCADE)

class TB_participantes(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField(11, primary_key=True)
    email = models.EmailField()
    senha = models.CharField(max_length=18)
    telefone = models.IntegerField(11)
    disturbio = models.TextField(null=True, blank=True)
    sala_inserido = models.ForeignKey(TB_salas, on_delete=models.CASCADE, null=True)



# Create your models here.
