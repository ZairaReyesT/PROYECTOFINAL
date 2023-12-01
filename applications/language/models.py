from django.db import models
from applications.country.models import Country

# Create your models here.
class Language(models.Model):
    Language = models.CharField(
        'Language',
        null=False,
        max_length=5,
    )

Isofficial = models.BooleanField(
    'Isofficial',
    null=False,
    default=False,
)

Percentage = models.BigIntegerField(
    'Percentage',
    null=False,
    max_length=20,
)

Sing_Language = models.CharField(
    'Sing_Language',
    null=False,
    max_length=1,
)

class Meta:
    verbose_name = 'Language'
    verbose_name_plural = 'Language'
def __str__(self):
    return self.Language+' ' + self.CLanguage + ' - ' + str(self.id)