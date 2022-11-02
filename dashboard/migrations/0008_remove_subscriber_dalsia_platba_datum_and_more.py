# Generated by Django 4.1.1 on 2022-10-04 06:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_alter_payinggroup_mesacne_na_cloveka'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='dalsia_platba_datum',
        ),
        migrations.AddField(
            model_name='payinggroup',
            name='dalsia_platba_datum',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
