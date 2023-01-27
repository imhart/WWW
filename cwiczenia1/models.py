from django.db import models
class book(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=12, decimal_places=2)
# Create your models here.
