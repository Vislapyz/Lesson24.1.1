# Generated by Django 5.0.6 on 2024-07-09 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vehicle", "0005_alter_milage_car_alter_milage_moto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="milage",
            name="car",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="milage",
                to="vehicle.car",
            ),
        ),
    ]
