from django.db import models
from uuid import uuid4

class ClienteModel(models.Model):
    # Model de clientes
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cpf = models.CharField(max_length=14, editable=False, null=False, blank=False)
    nome =  models.CharField(max_length=14, editable=False, null=False, blank=False)
    sexo  = models.CharField(max_length=1, editable=False, null=False, blank=False)
    email  =  models.CharField(max_length=255, editable=False, null=False, blank=False)
    dataDeNascimento = models.DateField(default=False,null=True,blank=True)
    rendaMensal = models.DecimalField(max_digits=5, decimal_places=3, default=False)

    class Meta:
        verbose_name = 'Cliente'
        db_table = 'Clientes'

    def __str__(self):
        return self.self.id