# Generated by Django 4.1.1 on 2022-09-24 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_subscriber_zaplatene_stav_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payinggroup',
            name='hex_color_without_hashtag',
            field=models.CharField(default='ffffff', max_length=6),
        ),
    ]
