from django.db import models
from django.utils.translation import gettext_lazy as _
# kod z oficjalnej dokumentacji Django
class Osoba(models.Model):
    imie = models.CharField(max_length=60 ,blank=False)
    nazwisko = models.CharField(max_length=60, blank=False)
    class Months(models.TextChoices):
        STYCZEN = 'I', _('Styczeń')
        LUTY = 'II', _('Luty')
        MARZEC = 'III', _('Marzec')
        KWIECIEN = 'IV', _('Kwiecień')
        MAJ = 'V', _('Maj')
        CZERWIEC = 'VI', _('Czerwiec')
        LIPIEC = 'VII', _('Lipiec')
        SIERPIEN = 'VIII', _('Sierpień')
        WRZESIEN = 'IX', _('Wrzesień')
        PAZDZIERNIK = 'X', _('Październik')
        LISTOPAD = 'XI', _('Listopad')
        GRUDZIEN = 'XII', _('Grudzień')

    miesiac_urodzenia = models.CharField(max_length=4,choices=Months.choices, default=Months.LUTY)
    data_dodania = models.DateField(auto_now=True)

    def __str__(self):
        return self.imie


# Create your models here.
