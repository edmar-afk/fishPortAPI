# Generated by Django 5.0.6 on 2024-11-21 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_vesselregistration_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vesselregistration',
            name='amount',
            field=models.TextField(default='554'),
        ),
    ]
