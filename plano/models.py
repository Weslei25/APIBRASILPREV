from django.db import models
from cliente.models import ClienteModel
from produto.models import ProdutoModel
from uuid import uuid4


class PlanoModel(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    idCliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE, null=False, blank=False)
    idProduto = models.ForeignKey(ProdutoModel, on_delete=models.CASCADE, null=False, blank=False)
    aporte = models.DecimalField(max_digits=10, decimal_places=1, default=False)
    dataDaContratacao = models.DateField(default=False,null=True,blank=True)

    class Meta:
        verbose_name = 'Plano'
        db_table = 'plano'

    def __str__(self):
        return self.self.id

class AporteExtraModel(models.Model):
    idCliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE, null=False, blank=False)
    idPlano = models.ForeignKey(PlanoModel, on_delete=models.CASCADE, null=False, blank=False)
    valorAporte = models.DecimalField(max_digits=10, decimal_places=1, default=False)

    class Meta:
        verbose_name = 'Aporte_Extra'
        db_table = 'apoete_extra'

    def __str__(self):
        return self.self.id

class ResgateModel(models.Model):
    idPlano = models.ForeignKey(PlanoModel, on_delete=models.CASCADE, null=False, blank=False)
    valorResgate = models.DecimalField(max_digits=10, decimal_places=1, default=False)

    class Meta:
        verbose_name = 'Resgate'
        db_table = 'resgate'

    def __str__(self):
        return self.self.id