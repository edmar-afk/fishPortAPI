# Generated by Django 5.0.6 on 2024-12-01 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_permitexpirationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weighin',
            name='date_weighin',
            field=models.DateField(auto_now_add=True),
        ),
    ]