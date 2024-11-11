# Generated by Django 5.0.6 on 2024-11-10 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_fisherman_fishermenregistration_fishingpermit_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fishingpermit',
            old_name='description',
            new_name='vessel_description',
        ),
        migrations.AddField(
            model_name='fishingpermit',
            name='owner_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='breadth',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='coast_guard_num',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='crew_num',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='cylinder_num',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='depth',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='draught',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='engine',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='engine_num',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='gross',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='home_port',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='horse_power',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='length',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='mfvr_num',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='net',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='serial_num',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='service_type',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='vessel_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='fishingpermit',
            name='vessel_type',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]