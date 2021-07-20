from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Ksiazka(models.Model):
    miekka = 'mk'
    twarda = 'twarda'
    Typ_okladki = {
        (miekka, 'miękka'),
        (twarda, 'twarda'),
    }
    tytul = models.CharField(max_length=32, default='')
    autor = models.CharField(max_length=32, default='')
    typ_okladki = models.CharField(max_length=32, choices=Typ_okladki, default=miekka)
    wydawnictwo = models.CharField(max_length=35, default='')
    data_premiery = models.DateField(auto_now_add=False, auto_now=False, blank=False, null=True)
    data_publikacji = models.DateTimeField(default=None)
    liczba_stron = models.IntegerField(default=1)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    zdjecie = models.ImageField(upload_to='okladki', default=None)

    def __str__(self):
        return self.tytul

