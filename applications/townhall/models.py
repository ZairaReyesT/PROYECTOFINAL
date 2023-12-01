from django.db import models
from applications.country.models import Country

# Create your models here.
class Townhall(models.Model):
    Townhall = models.CharField(
        'Townhall',
        null=False,
        max_length=5,
    )

    Mayor = models.CharField(
        'Mayor',
        null=False,
        max_length=30,
    )

    Councilor = models.CharField(
        'Councilor',
        null=False,
        max_length=30,
    )
    
    class Meta:
        verbose_name = 'Townhall'
        verbose_name_plural = 'Townhall'
    def __str__(self):
        return self.Townhall+' ' + self.Townhall + ' - ' + str(self.id)
    
