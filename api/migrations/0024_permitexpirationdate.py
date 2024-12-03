# Generated by Django 5.0.6 on 2024-11-22 02:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_alter_expirationdate_date_registered'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermitExpirationDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_registered', models.DateField(auto_now_add=True)),
                ('date_expired', models.DateField(blank=True)),
                ('permit_reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.fishingpermit')),
            ],
        ),
    ]
