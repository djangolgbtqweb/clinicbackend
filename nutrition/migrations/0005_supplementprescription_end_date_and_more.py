# Generated by Django 4.2.20 on 2025-05-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0004_remove_supplementprescription_patient_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplementprescription',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='supplementprescription',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
