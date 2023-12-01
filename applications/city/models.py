from django.db import models
from applications.country.models import Country

# Create your models here.
class City(models.Model):
    Id = models.CharField(
        'Id',
        null=False,
        max_length=5
    )

    Name = models.CharField(
        'Name',
        null=False,
        max_length=35
    )

    Id_Country = models.CharField(
        'Id_Country',
        null=False,
        max_length=3   
    )

    District = models.CharField(
        'District',
        null=False,
        max_length=20
    )

    Population = models.BigIntegerField(
        'Population',
        null=False,
        max_length=10
    )

    Taxes = models.CharField(
        'Taxes',
        null=False,
        max_length=20
    )

    Id_Townhall = models.CharField( 
        'Id_Townhall',
        null=False,
        max_length=5,
    )

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Citys'
    def __str__(self):
        return self.City+' ' + self.City + ' - ' + str(self.id)
        