# Generated by Django 5.1.4 on 2024-12-06 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_event_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='booking_event')),
                ('title', models.CharField(max_length=225)),
                ('short_description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'category',
                'ordering': ['-id'],
            },
        ),
    ]
