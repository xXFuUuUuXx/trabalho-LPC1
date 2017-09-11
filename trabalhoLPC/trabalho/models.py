from django.db import models


class Evento():
    nome = models.CharField(max_length=128)
    eventoPrincipal = models.CharField(max_length=128)
    sigla = models.CharField(max_length=20)
    dataEHoraDeInicio = models.DateField()
    palavrasChave = models.CharField(max_length=128)
    logotipo = models.CharField(max_length=50)
    realizador = models.ForeignKey(Pessoa)
    cidade = models.CharField(max_length=128)
    uf = models.CharField(max_length=2)
    endereco = models.CharField(max_length=128)
    cep = models.CharField(max_length=12)


class Pessoa():
    nome = models.CharField(max_length=128)
    email = models.CharField(max_legth=128)

class Artigo():
    nome=models.TextField()


class Autor(Pessoa):
    curriculo = models.CharField(max_length=128)
    artigos = models.ManyToManyField(Artigo)


class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=20)
    razaoSocial = models.CharField(max_length=128)


class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=11)


class EventoCientifico(Evento):
    issn = models.CharField(max_length=128)


class ArtigoCientifico():
    titulo = models.CharField(max_length=128)
    autores = models.ManyToManyField(Autor)

