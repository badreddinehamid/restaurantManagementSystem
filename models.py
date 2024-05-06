from django.db import models

class Reservation(models.Model):
    num_table  = models.IntegerField()
    nbr_chairs = models.IntegerField(default=1)

    class Meta :
        db_table = 'Reservation'
    

    def __str__(self) -> str:
        return f"reservation saved"


class Commande(models.Model):
    num_table = models.IntegerField()
    id_product = models.IntegerField()


    class Meta :
        db_table = "Commande"

    def __str__(self) -> str:
        return f"commande added ..."
    

class Product(models.Model):
    quantiry = models.IntegerField()
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta :
        db_table= "Product"

    def __str__(self) -> str:
        return f"product added"
