# Generated by Django 4.1.1 on 2022-10-04 06:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_remove_subscriber_dalsia_platba_datum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payinggroup',
            name='dalsia_platba_datum',
            field=models.DateField(default=datetime.date(2022, 10, 4)),
        ),
    ]
