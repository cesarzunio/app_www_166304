# Generated by Django 5.1.2 on 2024-11-14 01:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_person_data_dodania'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='data_dodania',
        ),
        migrations.AddField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
