# Generated by Django 5.2.1 on 2025-06-08 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_orderedfood_ordered_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedfood',
            name='food',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ordered_foods', to='app.food'),
        ),
    ]
