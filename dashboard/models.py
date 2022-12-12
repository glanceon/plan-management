from email.policy import default
from enum import unique
from django.db import models
from django.utils.timezone import now
from django.db.models.signals import pre_save, post_save
# Služba (Netflix, Spotify, NordVPN..)
class Service(models.Model):
    id = models.AutoField(primary_key=True)
    nazov_sluzby = models.CharField(max_length=60, null=True, default="sluzba")
    cely_nazov_sluzby = models.CharField(max_length=60, null=True, default="Názov služby")
    hex_color_without_hashtag = models.CharField(max_length=6, default="ffffff")

    def __str__(self):
        return self.cely_nazov_sluzby    

# Platiaca Skupina
class PayingGroup(models.Model):
    id = models.AutoField(primary_key=True)
    nazov_skupiny = models.CharField(max_length=60, null=True)
    mesacne_na_cloveka = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    dalsia_platba_datum = models.DateField(default=now())
    sluzba = models.ForeignKey(to=Service, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nazov_skupiny

# Platiteľ
class Subscriber(models.Model):
    id = models.AutoField(primary_key=True)
    meno = models.CharField(max_length=60, null=True)
    iban = models.CharField(max_length=60, null=True, unique=True)
    skupina = models.ManyToManyField(to=PayingGroup)
    dlh = models.DecimalField(null=True, max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.meno

# Platba
class Payment(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    datum_platby = models.DateField(null=True, default=now())
    platba_suma = models.DecimalField(null=True, max_digits=6, decimal_places=2, default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.subscriber.meno) + " " + str(self.platba_suma) + "€ " + str(self.datum_platby)

def payment_post_save(*args, **kwargs):
    return args, kwargs

post_save.connect(payment_post_save, sender=Payment)
