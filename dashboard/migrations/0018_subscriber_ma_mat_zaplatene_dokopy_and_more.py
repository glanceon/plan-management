# Generated by Django 4.1.1 on 2022-10-04 11:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_alter_payinggroup_dalsia_platba_datum_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='ma_mat_zaplatene_dokopy',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='payinggroup',
            name='dalsia_platba_datum',
            field=models.DateField(default=datetime.datetime(2022, 10, 4, 11, 9, 28, 363183, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='datum_platby',
            field=models.DateField(default=datetime.datetime(2022, 10, 4, 11, 9, 28, 365183, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
