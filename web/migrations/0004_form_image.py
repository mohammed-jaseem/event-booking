# Generated by Django 5.1.4 on 2024-12-10 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_form_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
