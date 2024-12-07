# Generated by Django 5.1.4 on 2024-12-05 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='booking_slider')),
                ('title', models.CharField(max_length=225)),
            ],
            options={
                'verbose_name': 'slider',
                'verbose_name_plural': 'sliders',
                'db_table': 'slider',
                'ordering': ['-id'],
            },
        ),
    ]
