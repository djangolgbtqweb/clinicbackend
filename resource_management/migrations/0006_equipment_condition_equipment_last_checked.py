# Generated by Django 4.2.20 on 2025-05-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource_management', '0005_rename_uantity_equipment_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='condition',
            field=models.CharField(choices=[('Good', 'Good'), ('Needs Repair', 'Needs Repair'), ('Broken', 'Broken')], default='Good', max_length=50),
        ),
        migrations.AddField(
            model_name='equipment',
            name='last_checked',
            field=models.DateField(blank=True, null=True),
        ),
    ]
