# Generated by Django 5.1.2 on 2024-11-14 01:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_stanowisko_osoba'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='data_dodania',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]