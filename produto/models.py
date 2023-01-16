from django.db import models
from uuid import uuid4
# Create your models here.

class ProdutoModel(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255, null=False, blank=False)
    susep = models.CharField(max_length=20, null=False, blank=False)
    expiracaoDeVenda = models.DateField(default=False,null=True,blank=True)
    valorMinimoAporteInicial =models.DecimalField(max_digits=10, decimal_places=1, default=False)
    valorMinimoAporteExtra = models.DecimalField(max_digits=10, decimal_places=1, default=False)
    idadeDeEntrada  = models.IntegerField(default=False, blank=True, null=True)
    idadeDeSaida  = models.IntegerField(default=False, blank=True, null=True)
    carenciaInicialDeResgate = models.IntegerField(default=False, blank=True, null=True)
    carenciaEntreResgates = models.IntegerField(default=False, blank=True, null=True)

    class Meta:
        verbose_name = 'Produto'
        db_table = 'produtos'

    def __str__(self):
        return f"{self.id}"