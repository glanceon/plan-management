from email.policy import default
from enum import unique
from django.db import models
from django.utils.timezone import now
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User


# Service (Netflix, Spotify, NordVPN..)


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    service_name = models.CharField(
        max_length=60, null=True, default="service")
    whole_service_name = models.CharField(
        max_length=60, null=True, default="Service name")
    hex_color_without_hashtag = models.CharField(
        max_length=6, default="ffffff")
    manager = models.ForeignKey(
        to=User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.whole_service_name

# Group of people paying for the same service


class PayingGroup(models.Model):
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=60, null=True)
    monthly_cost = models.DecimalField(
        null=True, max_digits=6, decimal_places=2)
    next_payment_date = models.DateField(default=now())
    service = models.ForeignKey(
        to=Service, on_delete=models.CASCADE, default=None)
    manager = models.ForeignKey(
        to=User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.group_name

# Member of family plan


class Subscriber(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60, null=True)
    iban = models.CharField(max_length=60, null=True, unique=True)
    group = models.ManyToManyField(to=PayingGroup)
    debt = models.DecimalField(null=True, max_digits=6,
                               decimal_places=2, default=0)
    manager = models.ForeignKey(
        to=User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

# Payment


class Payment(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    date_of_payment = models.DateField(null=True, default=now())
    paid_amount = models.DecimalField(
        null=True, max_digits=6, decimal_places=2, default=0)
    manager = models.ForeignKey(
        to=User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.subscriber.name) + " " + str(self.paid_amount) + "€ " + str(self.date_of_payment)


def payment_post_save(*args, **kwargs):
    return args, kwargs


post_save.connect(payment_post_save, sender=Payment)
