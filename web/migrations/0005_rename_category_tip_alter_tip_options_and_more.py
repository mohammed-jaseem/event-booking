# Generated by Django 5.1.4 on 2024-12-06 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Tip',
        ),
        migrations.AlterModelOptions(
            name='tip',
            options={'ordering': ['-id'], 'verbose_name': 'tip', 'verbose_name_plural': 'tips'},
        ),
        migrations.AlterModelTable(
            name='tip',
            table='tip',
        ),
    ]
