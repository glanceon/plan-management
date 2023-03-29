from decimal import Decimal
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Service (Netflix, Spotify, NordVPN..)


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    service_name = models.CharField(
        max_length=60, default="service", null=False)
    whole_service_name = models.CharField(
        max_length=60, default="Service name", null=False)
    hex_color_without_hashtag = models.CharField(
        max_length=6, default="ffffff", null=False)
    manager = models.ForeignKey(
        to=User, on_delete=models.CASCADE, default=None, null=False)

    def __str__(self):
        return self.whole_service_name

# Group of people paying for the same service


class PayingGroup(models.Model):
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(
        max_length=60, null=False, default="My group")
    monthly_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default="0")
    next_payment_date = models.DateField(auto_now_add=True)
    service = models.ForeignKey(
        to=Service, on_delete=models.CASCADE, default=None, null=False)
    manager = models.ForeignKey(
        to=User, on_delete=models.CASCADE, default=None, null=False)

    def __str__(self):
        return self.group_name

# Member of family plan


class Subscriber(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=60, default="Subscriber Name", null=False)
    iban = models.CharField(max_length=60, unique=True,
                            default="Subscriber Iban", null=False)
    group = models.ManyToManyField(to=PayingGroup)
    debt = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, null=False)
    manager = models.ForeignKey(
        to=User, on_delete=models.CASCADE, default=None, null=False)

    def __str__(self):
        return self.name

# Payment


class Payment(models.Model):
    subscriber = models.ForeignKey(
        Subscriber, on_delete=models.CASCADE, null=False)
    date_of_payment = models.DateField(
        auto_now_add=True)
    paid_amount = models.DecimalField(validators=[MinValueValidator(Decimal('0.00'))],
                                      max_digits=6, decimal_places=2, default=0, null=False)
    manager = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.subscriber.name + " " + str(self.paid_amount) + "€ " + str(self.date_of_payment)


def payment_post_save(*args, **kwargs):
    return args, kwargs


post_save.connect(payment_post_save, sender=Payment)
