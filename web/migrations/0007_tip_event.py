# Generated by Django 5.1.4 on 2024-12-06 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_tip_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.event'),
            preserve_default=False,
        ),
    ]
