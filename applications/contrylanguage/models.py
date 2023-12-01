from django.db import models
from applications.country.models import Country

class CountryLanguage(models.Model):
    Id_CountryLanguage = models.CharField(
        'Id_CountryLanguage',
        null=False,
        max_length=5,
    )

    Id_Country = models.CharField(
        'Id_Country',
        null=False,
        max_length=5,
    )

    Id_Language = models.CharField(
        'Id_Language',
        null=False,
        max_length=5,
    )

    class Meta:
        verbose_name = 'CountryLanguage'
        verbose_name_plural = 'CountryLanguage'
    def __str__(self):
        return self.CountryLanguage+' ' + self.CountryLanguage + ' - ' + str(self.id)