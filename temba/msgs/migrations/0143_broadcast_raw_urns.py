# Generated by Django 2.2.10 on 2020-10-01 18:17

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("msgs", "0142_auto_20200929_1734"),
    ]

    operations = [
        migrations.AddField(
            model_name="broadcast",
            name="raw_urns",
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None),
        ),
    ]
