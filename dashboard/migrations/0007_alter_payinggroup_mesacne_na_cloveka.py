# Generated by Django 4.1.1 on 2022-10-04 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_payinggroup_sluzba'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payinggroup',
            name='mesacne_na_cloveka',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
