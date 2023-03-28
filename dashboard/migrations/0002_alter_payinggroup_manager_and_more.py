# Generated by Django 4.1.1 on 2023-03-24 14:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payinggroup',
            name='manager',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='payinggroup',
            name='next_payment_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 24, 14, 10, 51, 196953, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date_of_payment',
            field=models.DateField(default=datetime.datetime(2023, 3, 24, 14, 10, 51, 198962, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='manager',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='manager',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]
