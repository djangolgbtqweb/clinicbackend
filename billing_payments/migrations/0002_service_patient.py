# Generated by Django 4.2.17 on 2025-04-26 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
        ('billing_payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='patients.patient'),
        ),
    ]
