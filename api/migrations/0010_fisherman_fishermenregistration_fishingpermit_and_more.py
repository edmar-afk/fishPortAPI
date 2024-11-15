# Generated by Django 5.0.6 on 2024-11-10 02:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_rename_price_weighin_price_per_kilo_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fisherman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_num', models.IntegerField()),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FishermenRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fishermen_registrations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FishingPermit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True)),
                ('home_port', models.TextField(blank=True)),
                ('vessel_name', models.TextField(blank=True)),
                ('vessel_type', models.TextField(blank=True)),
                ('color', models.TextField(blank=True)),
                ('service_type', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('length', models.TextField(blank=True)),
                ('breadth', models.TextField(blank=True)),
                ('depth', models.TextField(blank=True)),
                ('draught', models.TextField(blank=True)),
                ('gross', models.TextField(blank=True)),
                ('net', models.TextField(blank=True)),
                ('engine', models.TextField(blank=True)),
                ('serial_num', models.TextField(blank=True)),
                ('horse_power', models.TextField(blank=True)),
                ('cylinder_num', models.TextField(blank=True)),
                ('engine_num', models.TextField(blank=True)),
                ('crew_num', models.TextField(blank=True)),
                ('coast_guard_num', models.TextField(blank=True)),
                ('mfvr_num', models.TextField(blank=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fishing_permits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VesselRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_address', models.TextField()),
                ('year_built', models.DateField()),
                ('length', models.TextField()),
                ('breadth', models.TextField()),
                ('depth', models.TextField()),
                ('draught', models.TextField()),
                ('gross', models.TextField()),
                ('net', models.TextField()),
                ('hull_material', models.TextField()),
                ('mast', models.TextField()),
                ('color', models.TextField()),
                ('stern', models.TextField()),
                ('crew_num', models.TextField()),
                ('serial_num', models.TextField()),
                ('cycle', models.TextField()),
                ('cylander_num', models.TextField()),
                ('engine_num', models.TextField()),
                ('former_owner', models.TextField()),
                ('address', models.TextField()),
                ('owner_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vessel_registrations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
