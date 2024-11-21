# Generated by Django 5.0.6 on 2024-11-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_vesselregistration_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='vesselregistration',
            name='home_port',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='vesselregistration',
            name='service_type',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='vesselregistration',
            name='vessel_name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='weighin',
            name='price_per_kilo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weighin',
            name='total_price',
            field=models.TextField(blank=True, null=True),
        ),
    ]
