# Generated by Django 5.2.1 on 2025-06-13 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_ordering_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordering',
            name='table_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table', to='app.table'),
        ),
    ]
