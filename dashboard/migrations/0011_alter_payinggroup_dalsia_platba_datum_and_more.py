# Generated by Django 4.1.1 on 2022-10-04 07:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_remove_subscriber_platba_payment_datum_platby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payinggroup',
            name='dalsia_platba_datum',
            field=models.DateField(default=datetime.datetime(2022, 10, 4, 7, 30, 2, 737168, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='datum_platby',
            field=models.DateField(default=datetime.datetime(2022, 10, 4, 7, 30, 2, 739201, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
