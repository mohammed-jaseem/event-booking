# Generated by Django 5.1.4 on 2024-12-06 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_rename_category_tip_alter_tip_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='name',
            field=models.CharField(default=1, max_length=225),
            preserve_default=False,
        ),
    ]
