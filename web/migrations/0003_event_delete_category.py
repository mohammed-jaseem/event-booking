# Generated by Django 5.1.4 on 2024-12-06 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_category_alter_slider_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='booking_event')),
                ('name', models.CharField(max_length=225)),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
                'db_table': 'event',
                'ordering': ['-id'],
            },
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]