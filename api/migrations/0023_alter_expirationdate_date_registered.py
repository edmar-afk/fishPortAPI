# Generated by Django 5.0.6 on 2024-11-22 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_expirationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expirationdate',
            name='date_registered',
            field=models.DateField(auto_now_add=True),
        ),
    ]
