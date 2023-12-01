from django.db import models

# Create your models here.
class Country(models.Model):
    Id_Country = models.CharField(
        'Id_Country',
        null=False,
        max_length=5,
    )

    Name = models.CharField(
        'Name',
        null=False,
        max_length=30,
    )

    Continent = models.CharField(
        'Continent',
        null=False,
        max_length=30,
    )

    Region = models.CharField(
        'Region',
        null=False,
        max_length=30,
    )

    SurFacearea = models.BigIntegerField(
        'SurFacearea',
        null=False,
        max_length=20,
)
    
    Indepyear = models.DateField(
       'Indepyear',
       null=False,
       default='', 
    )

    LifeExpectancy = models.CharField(
        'LifeExpectancy',
        null=False,
        max_length=50
    )

    GNP = models.DecimalField(
        'GNP',
        null=False,
        max_length=10.2,
        max_digits=11,
        max_places=1,
    )

    GNPold = models.DecimalField(
        'GNPold',
        null=False,
        max_length=10.2,
        max_digits=11,
        max_places=1,
    )

    LocalName = models.CharField(
        'LocalName',
        null=False,
        max_length=25,
    )

    Governmentform = models.CharField(
        'Governmentform',
        null=False,
        max_length=25,
    )

    Headofstate = models.CharField(
        'Headofstate',
        null=False,
        max_length=25,
    )

    Capital = models.CharField(
        'Capital',
        null=False,
        max_length=25,
    )

    Code2 = models.CharField(
        'Code2',
        null=False,
        max_length=5,
    )

    Migration = models.CharField(
        'Migration',
        null=False,
        max_length=50,
    )

    Poverty = models.CharField(
        'Poverty',
        null=False,
        max_length=50,
    )

class Meta:
    verbose_name = 'Country'
    verbose_name_plural = 'Countrys'
def __str__(self):
    return self.Country+' ' + self.Country + ' - ' + str(self.id)