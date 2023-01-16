from django.db import models
from cliente.models import ClienteModel
from produto.models import ProdutoModel
from uuid import uuid4
from datetime import date

class PlanoModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, auto_created=True)
    produto = models.ForeignKey(ProdutoModel, on_delete=models.CASCADE)
    cliente = models.ForeignKey(ClienteModel, related_name='tracks', on_delete=models.CASCADE, )
    aporte = models.DecimalField(max_digits=10, decimal_places=3, default=False)
    dataDaContratacao = models.DateField(default=date.today,null=True,blank=True)

    class Meta:
        verbose_name = 'Plano'
        db_table = 'plano'

    def __str__(self):
        return f'{self.dataDaContratacao}'

class AporteExtraModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE, null=False, blank=False)
    plano = models.ForeignKey(PlanoModel, on_delete=models.CASCADE, null=False, blank=False)
    valorAporte = models.DecimalField(max_digits=10, decimal_places=3, default=False)

    class Meta:
        verbose_name = 'Aporte_Extra'
        db_table = 'apoete_extra'

    def __str__(self):
        return self.Cliente

class ResgateModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    plano = models.ForeignKey(PlanoModel, on_delete=models.CASCADE, null=False, blank=False)
    valorResgate = models.DecimalField(max_digits=10, decimal_places=3, default=False)

    class Meta:
        verbose_name = 'Resgate'
        db_table = 'resgate'

    def __str__(self):
        return self.Plano