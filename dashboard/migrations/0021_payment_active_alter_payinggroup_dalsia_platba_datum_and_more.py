# Generated by Django 4.1.1 on 2022-11-15 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_alter_payinggroup_dalsia_platba_datum_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='payinggroup',
            name='dalsia_platba_datum',
            field=models.DateField(default=datetime.datetime(2022, 11, 15, 14, 47, 33, 278832, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='datum_platby',
            field=models.DateField(default=datetime.datetime(2022, 11, 15, 14, 47, 33, 280834, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
