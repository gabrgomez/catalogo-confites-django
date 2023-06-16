from django.db import models

class TipoConfite(models.Model):
    id = models.AutoField(primary_key=True, db_column='CtgTpoCftID')
    nombre = models.CharField(max_length=50, db_column='CtgTpoCftNom')

    class Meta:
        db_table = 'CtgTpoCft'

    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True,db_column='CtgProdCod')
    nombre = models.CharField(max_length=20, db_column='CtgProdNom')
    imagen = models.ImageField(upload_to='catalogo/producto', db_column='CtgProdImg')
    precio = models.PositiveIntegerField(db_column='CtgProdPre')
    fch_elab = models.DateField(db_column='CtgProdFlb')
    fch_vence = models.DateField(db_column='CtgProdFVen')
    tipo = models.ForeignKey(to = TipoConfite, on_delete=models.CASCADE, db_column='CtgTpoCftID')


    class Meta:
        db_table = 'CtgProd'

    def __str__(self) -> str:
        return self.nombre
