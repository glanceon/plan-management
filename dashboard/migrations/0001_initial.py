# Generated by Django 4.1.1 on 2022-09-20 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PayingGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nazov_skupiny', models.CharField(max_length=60)),
                ('mesacne_na_cloveka', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('meno', models.CharField(max_length=60)),
                ('zaplatene_stav', models.BooleanField(default=False)),
                ('zaplatene_dokopy', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('dlh', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('dalsia_platba_datum', models.DateField(null=True)),
                ('posledna_platba', models.DateField(null=True)),
                ('skupina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.payinggroup')),
            ],
        ),
    ]
