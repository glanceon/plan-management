# Generated by Django 4.1.1 on 2022-10-04 07:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_payinggroup_dalsia_platba_datum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='platba',
        ),
        migrations.AddField(
            model_name='payment',
            name='datum_platby',
            field=models.DateField(default=datetime.date(2022, 10, 4), null=True),
        ),
    ]
