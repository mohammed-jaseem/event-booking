# Generated by Django 5.1.4 on 2024-12-11 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='booking_project')),
                ('name', models.CharField(max_length=225)),
                ('date_time', models.DateTimeField()),
                ('place', models.CharField(max_length=225)),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
                'db_table': 'project',
                'ordering': ['-id'],
            },
        ),
    ]
