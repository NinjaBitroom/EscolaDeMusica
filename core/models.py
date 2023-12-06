from django.db import models


# Create your models here.
class Sinfonia(models.Model):
    nome = models.CharField(max_length=100)
    compositor = models.CharField(max_length=100)
    data_criacao = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Musico(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    nacionalidade = models.CharField(max_length=100, null=True, blank=True)
    nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Funcao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Instrumento(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    modelo = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome


class Orquestra(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, null=True, blank=True)
    data_criacao = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Executa(models.Model):
    desempenho = models.CharField(max_length=100, null=True, blank=True)
    orquestra = models.ForeignKey(Orquestra, on_delete=models.CASCADE)
    sinfonia = models.ForeignKey(Sinfonia, on_delete=models.CASCADE)

    def __str__(self):
        return self.orquestra.nome


class AptoA(models.Model):
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE)
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE)

    def __str__(self):
        return self.musico.nome


class Apresenta(models.Model):
    data = models.DateField()
    sinfonia = models.ForeignKey(Sinfonia, on_delete=models.CASCADE)
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE)
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE)

    def __str__(self):
        return self.musico.nome


class Compoe(models.Model):
    orquestra = models.ForeignKey(Orquestra, on_delete=models.CASCADE)
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE)
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE)

    def __str__(self):
        return self.musico.nome


class Usa(models.Model):
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE)
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)

    def __str__(self):
        return self.funcao.nome
